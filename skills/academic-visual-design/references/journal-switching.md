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

## Preserve the comparison while switching

Start from the supplied artifact, not a blank destination template. Read it at delivery size and identify what already supports the reader's comparison: grouping and adjacency, shared scales, category order, semantic encodings, and the placement of definitions and denominators. Treat effective choices as the baseline to retain, not as features to erase for a new house style.

Before editing, distinguish required changes, optional recommendations, and observed reading problems. For each planned change, identify the applicable rule or concrete problem it addresses; otherwise retain the current choice. A requirement for explicit denominators does not by itself require repeating a shared total in every cell. A naming or export requirement does not require rebuilding a plot. Do not flatten meaningful headings or change representation merely to make versions look different.

Apply each requirement at the smallest useful scope. If a rule genuinely conflicts with the existing structure, adapt that part and preserve the comparison by another means. Existing defects may be corrected, but explain the specific defect rather than treating conversion as unrestricted redesign.

Compare the source and destination renders using the same reader question. Check whether values that belonged together still do, whether decoding now requires extra lookup, and whether a delivery-only change altered the display. Reverse avoidable regressions. Keep a brief change-and-reason record in existing notes or the handoff; retained structure is a valid outcome. Do not manufacture alternative layouts for an otherwise sound conversion.


## Verify requirements in the delivered format

Before implementing a conversion, put a compact per-destination constraint map in existing working notes or code: the applicable requirement, the source/shared default it overrides, and how to check the delivered artifact. Include prohibitions, not only required additions. Keep destination overrides distinct when generating several formats; a shared styling function must not silently reapply a forbidden convention.

Check negative requirements by inspecting absence in both the visible output and native formatting. For example, an instruction not to draw rules excludes retained top, header and bottom rules too; inspect table-level and cell-level borders rather than assuming a familiar three-line table is exempt. Likewise, a prohibition on abbreviated headings includes grouped headings. Preserve the comparison using permitted spacing and emphasis when a familiar separator is unavailable.

Close each applicable check against the final deliverable as satisfied, violated or unverified, with brief evidence in the existing handoff or code notes. Fix an observed violation before calling the conversion complete; if it cannot be fixed, identify the affected output. A generator setting or a declaration of compliance is not a check of the exported artifact.

Review the file the recipient will use. A browser table is not proof of a Word table's layout: conversion can change merged headings, emphasis, widths, borders and line breaks. Render the final native file at its intended page size with a compatible application when available. Check grouped headings and their visual separation from data, plus the longest labels and numeric entries. Keep a value and its interval readable together; use available column width and sensible spacing before reducing type or flattening the hierarchy.

Complete the visual review yourself before handoff. Exporting a PDF, counting its pages, extracting its text, or creating a screenshot does not mean you have looked at it. Open the final rendered pages with an image-viewing tool and inspect their visible content. For a Word deliverable, export that exact DOCX with a compatible application, rasterize the resulting PDF if necessary, and view those page images. Use the available local renderer and image viewer; do not leave this step to a downstream reviewer when you can perform it.

Reserve time for that inspection before optional polish. Review each distinct destination layout, including its last page. In existing notes or the handoff, identify the native file and preview actually viewed, one concrete visible finding (or the specific locations checked if no defect is found), and whether a correction was needed. This is a short evidence trail, not a new report.

After a repair, regenerate and view the affected native export again; inspection of an earlier preview does not cover later layout changes. Keep source evidence and required formatting intact. If rendering or image viewing is genuinely unavailable or fails, report the attempted operation and the remaining review gap; mark the affected deliverable provisional rather than calling its visual review complete.
