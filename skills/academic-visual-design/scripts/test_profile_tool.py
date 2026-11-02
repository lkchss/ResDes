import copy
import unittest
import profile_tool as tool


def sample():
    return {'schema_version': 1, 'id': 'test', 'title': 'Synthetic test', 'scope': {'publication': 'Synthetic', 'article_types': ['research'], 'stages': ['initial', 'revision', 'final']}, 'coverage_note': 'Partial synthetic profile', 'sources': [{'id': 's', 'url': 'https://example.org', 'title': 'Synthetic', 'accessed_on': '2026-01-01', 'verification_state': 'verified'}], 'rules': [rule()]}


def rule(key='table.columns', value=9, stage='all', strength='requirement'):
    return {'id': key, 'key': key, 'summary': 'Synthetic rule', 'source_id': 's', 'source_summary': 'Synthetic evidence', 'verified_on': '2026-01-01', 'verification_state': 'verified', 'strength': strength, 'applicability': {'stages': [stage], 'artifacts': ['table']}, 'constraint': {'kind': 'max', 'value': value, 'unit': 'columns'}}


class ProfilesTest(unittest.TestCase):
    def test_bundled_profiles_validate(self):
        for path in tool.ROOT.glob('*.json'):
            with self.subTest(path=path): self.assertEqual(tool.validate(tool.load(path)), [])

    def test_stage_and_artifact_filter(self):
        a = sample(); b = sample(); a['rules'][0]['applicability']['stages'] = ['final']; b['rules'][0]['constraint']['value'] = 4
        self.assertEqual(tool.compare(a, b, 'initial', 'figure')['changed'], [])
        self.assertTrue(tool.compare(a, b, 'initial', 'table')['unresolved'])
        self.assertEqual(len(tool.compare(a, b, 'final', 'table')['changed']), 1)

    def test_strength_change_is_not_equated(self):
        a = sample(); b = sample(); b['rules'][0]['strength'] = 'recommendation'
        result = tool.compare(a, b, 'initial', 'table')
        self.assertIn('incomparable requirement and recommendation', str(result))
        self.assertFalse(result['changed'])

    def test_context_unknown_and_source_only_never_relaxed(self):
        a = sample(); b = sample(); b['rules'][0]['key'] = 'other'; b['rules'][0]['constraint'] = None
        report = tool.compare(a, b, 'initial', 'table')
        text = str(report).lower()
        self.assertIn('absence is not permission to relax', text)
        self.assertIn('contextual or unknown', text)
        self.assertIn('not a compliance assessment', text)
        self.assertIn('no evidence or artifact was modified', text)
        self.assertEqual(report['changed'], [])

    def test_unverified_and_conflicts_remain_unresolved(self):
        a = sample(); b = sample(); b['rules'][0]['verification_state'] = 'unverified'; b['rules'][0]['verified_on'] = None
        other = copy.deepcopy(a['rules'][0]); other['id'] = 'conflict'; other['constraint']['value'] = 3; a['rules'].append(other)
        result = tool.compare(a, b, 'initial', 'table')
        self.assertIn('manual review', str(result)); self.assertIn('unverified', str(result)); self.assertFalse(result['changed'])

    def test_validation_rejects_missing_constraint_and_false_verification(self):
        a = sample(); del a['rules'][0]['constraint']; self.assertTrue(tool.validate(a))
        a = sample(); a['sources'][0]['verification_state'] = 'unverified'; a['sources'][0]['accessed_on'] = None
        self.assertTrue(tool.validate(a))

    def test_incomparable_types_and_units(self):
        a = sample(); b = sample(); b['rules'][0]['constraint']['unit'] = 'pixels'
        result = tool.compare(a, b, 'initial', 'table')
        self.assertIn('incomparable', str(result)); self.assertFalse(result['changed'])

    def test_malformed_shapes_report_errors_instead_of_crashing(self):
        a = sample(); a['scope']['stages'] = [[]]
        self.assertTrue(tool.validate(a))
        a = sample(); a['rules'][0]['source_id'] = []
        self.assertTrue(tool.validate(a))
        a = sample(); a['rules'][0]['constraint']['kind'] = []
        self.assertTrue(tool.validate(a))

    def test_nonfinite_numbers_rejected(self):
        for value in (float('nan'), float('inf'), float('-inf')):
            a = sample(); a['rules'][0]['constraint']['value'] = value
            self.assertTrue(tool.validate(a))
            a['rules'][0]['constraint'] = {'kind': 'one_of', 'value': [1, value], 'unit': None}
            self.assertTrue(tool.validate(a))

    def test_compatible_bounds_are_not_asserted_to_conflict(self):
        a = sample(); b = sample()
        extra = copy.deepcopy(a['rules'][0]); extra['id'] = 'second-bound'; extra['constraint']['value'] = 8
        a['rules'].append(extra)
        result = tool.compare(a, b, 'final', 'table')
        self.assertIn('manual review', str(result))
        self.assertNotIn('conflicting applicable rules', str(result))
        self.assertFalse(result['changed'])


if __name__ == '__main__': unittest.main()
