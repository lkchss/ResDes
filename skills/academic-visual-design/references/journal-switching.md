# Journal switching and submission requirements

Confirm the exact journal or manual, article type, submission stage, artifact and requested formats. Check editor instructions supplied for the article first, then current official guidance for the precise destination and stage. A profile is partial evidence, not a complete manual: inspect its scope, coverage note, source URLs, verification state and dates. Determine freshness against the current official guidance; an old access date alone does not prove a rule changed. Check current authoritative guidance when accuracy or submission readiness depends on it, and flag inaccessible or unverified rules.

Bundled profiles are `profiles/apa7.json`, `profiles/jama.json`, `profiles/ieee.json`, `profiles/nature.json` and `profiles/aer.json`; each states its own exact scope. Do not generalize a profile to another journal, publisher portfolio, article type or stage. For an unknown destination, research current official guidance or use guidelines the user supplies. If neither is available, produce useful provisional work where possible and enumerate the unverified requirements.

The optional standard-library helper compares profile metadata; run from the skill directory, using its help for exact arguments:

```text
python scripts/profile_tool.py validate --help
python scripts/profile_tool.py diff --help
```

For comparison, select the source and destination profiles and specify `--stage initial|revision|final` and `--artifact figure|table`. Review the resulting applicable differences, including strength, unresolved gaps and conflicts, against the actual artifact and official sources. A null constraint is contextual, not automatically satisfied. Profile validation and diff do not inspect the artifact or prove journal compliance.

Treat evidence as invariant while adapting presentation and delivery. Identify changes required by the destination, recommendation-only changes, unresolved information and conflicts; retain source data and document any interpretation-affecting change. Specific applicable requirements override broader defaults and aesthetic preferences; surface contradictions for resolution. Report the destination, article type, stage, sources and dates actually checked, artifact checks performed, remaining unknowns and any chosen deviation. Do not claim complete compliance without verifying all applicable instructions and the actual deliverables.
