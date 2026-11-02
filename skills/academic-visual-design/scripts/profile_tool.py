"""Validate partial journal profiles and compare their stated, applicable rules.

This tool inspects metadata only. It neither edits artifacts nor assesses compliance.
"""
import argparse
import datetime as dt
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent / 'profiles'
STAGES = {'initial', 'revision', 'final'}
ARTIFACTS = {'figure', 'table'}
KINDS = {'min', 'max', 'equals', 'one_of', 'required', 'prohibited'}


def validate(p):
    errors = []
    def check(condition, message):
        if not condition: errors.append(message)
    check(isinstance(p, dict), 'profile must be an object')
    if not isinstance(p, dict): return errors
    check(p.get('schema_version') == 1, 'schema_version must be 1')
    for key in ('id', 'title', 'coverage_note'):
        check(isinstance(p.get(key), str) and bool(p[key].strip()), f'{key} must be nonempty text')
    check('partial' in str(p.get('coverage_note', '')).lower(), 'coverage_note must say partial')
    scope = p.get('scope')
    check(isinstance(scope, dict), 'scope must be an object')
    if isinstance(scope, dict):
        check(isinstance(scope.get('publication'), str) and bool(scope['publication']), 'scope.publication required')
        check(isinstance(scope.get('article_types'), list) and bool(scope['article_types']) and all(isinstance(x, str) and x for x in scope['article_types']), 'scope.article_types required')
        check(isinstance(scope.get('stages'), list) and bool(scope['stages']) and all(isinstance(x, str) and x in STAGES for x in scope['stages']), 'invalid scope.stages')
    sources = p.get('sources')
    check(isinstance(sources, list) and bool(sources), 'sources must be nonempty list')
    source_map = {}
    def date_ok(value):
        if not isinstance(value, str): return False
        try: return dt.date.fromisoformat(value).isoformat() == value
        except ValueError: return False
    for s in sources if isinstance(sources, list) else []:
        if not isinstance(s, dict): errors.append('source must be object'); continue
        sid = s.get('id')
        check(isinstance(sid, str) and bool(sid) and sid not in source_map, 'source id missing or duplicate')
        if isinstance(sid, str): source_map[sid] = s
        check(isinstance(s.get('title'), str) and bool(s['title']), f'{sid}: source title required')
        check(isinstance(s.get('url'), str) and s['url'].startswith('https://'), f'{sid}: HTTPS source required')
        check(s.get('verification_state') in ('verified', 'unverified'), f'{sid}: invalid verification state')
        check((date_ok(s.get('accessed_on')) if s.get('verification_state') == 'verified' else s.get('accessed_on') is None), f'{sid}: inconsistent access date')
    rules = p.get('rules')
    check(isinstance(rules, list) and bool(rules), 'rules must be nonempty list')
    ids = set()
    for r in rules if isinstance(rules, list) else []:
        if not isinstance(r, dict): errors.append('rule must be object'); continue
        rid = r.get('id')
        check(isinstance(rid, str) and bool(rid) and rid not in ids, 'rule id missing or duplicate')
        if isinstance(rid, str): ids.add(rid)
        for key in ('key', 'summary', 'source_summary'):
            check(isinstance(r.get(key), str) and bool(r[key].strip()), f'{rid}: {key} required')
        source_id = r.get('source_id')
        source = source_map.get(source_id) if isinstance(source_id, str) else None
        check(source is not None, f'{rid}: unknown source')
        state = r.get('verification_state')
        check(state in ('verified', 'unverified'), f'{rid}: invalid verification state')
        check((date_ok(r.get('verified_on')) and source is not None and source.get('verification_state') == 'verified' if state == 'verified' else r.get('verified_on') is None), f'{rid}: inconsistent verification date/source')
        check(r.get('strength') in ('requirement', 'recommendation'), f'{rid}: invalid strength')
        app = r.get('applicability')
        check(isinstance(app, dict), f'{rid}: applicability required')
        if isinstance(app, dict):
            for key, allowed in [('stages', STAGES | {'all'}), ('artifacts', ARTIFACTS | {'all'})]:
                vals = app.get(key)
                check(isinstance(vals, list) and bool(vals) and all(isinstance(v, str) and v in allowed for v in vals), f'{rid}: invalid {key}')
        check('constraint' in r, f'{rid}: missing constraint (use null for contextual)')
        constraint = r.get('constraint')
        if constraint is not None:
            check(isinstance(constraint, dict), f'{rid}: constraint must be object or null')
            if isinstance(constraint, dict):
                kind = constraint.get('kind'); value = constraint.get('value'); unit = constraint.get('unit')
                check(isinstance(kind, str) and kind in KINDS, f'{rid}: invalid constraint kind')
                check('unit' in constraint and (unit is None or isinstance(unit, str)), f'{rid}: invalid unit')
                def scalar_ok(v):
                    return isinstance(v, (str, bool, int, float)) and (not isinstance(v, float) or math.isfinite(v))
                valid_scalar = scalar_ok(value)
                check((isinstance(value, list) and bool(value) and all(scalar_ok(v) for v in value)) if kind == 'one_of' else valid_scalar, f'{rid}: invalid constraint value')
                if kind in ('min', 'max'): check(isinstance(value, (int, float)) and not isinstance(value, bool), f'{rid}: bound must be numeric')
                if kind in ('required', 'prohibited'): check(value is True, f'{rid}: required/prohibited value must be true')
    return errors


def applies(r, stage, artifact):
    a = r['applicability']
    return (stage in a['stages'] or 'all' in a['stages']) and (artifact in a['artifacts'] or 'all' in a['artifacts'])


def compare(left, right, stage, artifact):
    result = {'notice': 'Partial metadata comparison only; this is not a compliance assessment. No evidence or artifact was modified.',
              'checked_scope': {'stage': stage, 'artifact': artifact, 'stage_note': 'The selected stage is compared on both sides; source-to-target stage changes were not examined.', 'from': left['scope'], 'to': right['scope']},
              'source_freshness': {}, 'changed': [], 'unresolved': []}
    for side, profile in [('from', left), ('to', right)]:
        result['source_freshness'][side] = [{'id': s['id'], 'url': s['url'], 'accessed_on': s['accessed_on'], 'verification_state': s['verification_state']} for s in profile['sources']]
        if stage not in profile['scope']['stages']:
            result['unresolved'].append({'side': side, 'reason': 'selected stage outside declared scope'})
    groups = []
    for profile in (left, right):
        grouped = {}
        for r in profile['rules']:
            if applies(r, stage, artifact): grouped.setdefault(r['key'], []).append(r)
        groups.append(grouped)
    for key in sorted(set(groups[0]) | set(groups[1])):
        a, b = groups[0].get(key, []), groups[1].get(key, [])
        entry = {'key': key, 'from': a, 'to': b}
        reasons = []
        if not a or not b: reasons.append('missing applicable rule; absence is not permission to relax a requirement')
        for side, rules in [('from', a), ('to', b)]:
            if any(r['verification_state'] != 'verified' for r in rules): reasons.append(f'{side}: unverified')
            if any(r['constraint'] is None for r in rules): reasons.append(f'{side}: contextual or unknown constraint')
            signatures = {(json.dumps(r['constraint'], sort_keys=True), r['strength']) for r in rules if r['constraint'] is not None and r['verification_state'] == 'verified'}
            if len(signatures) > 1: reasons.append(f'{side}: multiple differing applicable constraints require manual review; compatibility was not solved')
        if len(a) == len(b) == 1 and a[0]['constraint'] is not None and b[0]['constraint'] is not None:
            ca, cb = a[0]['constraint'], b[0]['constraint']
            if a[0]['strength'] != b[0]['strength']:
                reasons.append('incomparable requirement and recommendation; resolve manually')
            if ca['kind'] != cb['kind'] or ca['unit'] != cb['unit']:
                reasons.append('incomparable constraint kinds or units')
        if reasons:
            result['unresolved'].append({**entry, 'reasons': reasons})
        elif len(a) == len(b) == 1 and (a[0]['constraint'] != b[0]['constraint'] or a[0]['strength'] != b[0]['strength']):
            result['changed'].append(entry)
    return result


def load(path):
    with open(path, encoding='utf-8') as f: profile = json.load(f)
    errors = validate(profile)
    if errors: raise ValueError('; '.join(errors))
    return profile


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    v = sub.add_parser('validate'); v.add_argument('paths', nargs='*')
    d = sub.add_parser('diff'); d.add_argument('from_path'); d.add_argument('to_path'); d.add_argument('--stage', required=True, choices=sorted(STAGES)); d.add_argument('--artifact', required=True, choices=sorted(ARTIFACTS))
    args = parser.parse_args(argv)
    try:
        if args.command == 'validate':
            paths = [Path(x) for x in args.paths] if args.paths else sorted(ROOT.glob('*.json'))
            if not paths: raise ValueError('no profiles found')
            failures = 0
            for path in paths:
                try: load(path); print(f'OK {path} (partial profile; metadata validation only)')
                except (OSError, ValueError, json.JSONDecodeError) as e: print(f'ERROR {path}: {e}', file=sys.stderr); failures += 1
            return 1 if failures else 0
        print(json.dumps(compare(load(args.from_path), load(args.to_path), args.stage, args.artifact), indent=2, ensure_ascii=False))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(f'ERROR: {e}', file=sys.stderr); return 1


if __name__ == '__main__': sys.exit(main())
