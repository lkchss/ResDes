---
name: academic-visual-design
description: Create, critique, refine, or convert scholarly figures and tables while preserving scientific meaning and accounting for publication requirements.
---

# Academic visual design

Make evidence legible and publication-ready without changing what it says. Work in the user's existing toolchain when practical; use code and data for reproducible quantitative graphics, and preserve editable tables when the destination requires them. Do not use generative image models to fabricate or render evidence-bearing quantitative plots.

## Establish the task

Identify the requested artifact, audience, source material, intended toolchain and output. For venue-specific compliance, establish the **exact journal or style manual, article type and stage** (initial, revision or final); do not infer one journal's requirements for a family of titles. For a general manuscript draft, follow its established conventions and the requested output format. Ask for missing destination details only when the request requires venue-specific compliance. Otherwise proceed with defensible design choices; ask about missing scientific facts or explicit delivery constraints that affect correctness. Mark unverified requirements and choices.

When the artifact depends on research materials, first read [research context](references/research-context.md). Orient to the study, trace the requested result to its data/analysis source, and reconcile artifact-critical definitions before choosing a design. Reuse known context for cosmetic edits. Keep a small working brief; do not require a new user questionnaire or research report.

Keep three layers distinct:

- **Evidence:** underlying unrounded values, sample sizes and denominators, uncertainty identity, type and level, units, category and semantic mapping, transformations, missingness and exclusions, and sources.
- **Design:** representation, panel order, semantic color, typography, spacing, labels and table hierarchy.
- **Publication:** exact destination, article type and stage, applicable requirements, source dates and delivery format.

Preserve the evidence layer across redesigns and conversions. Presentation rounding must not replace underlying values. Explain any unit conversion, changed estimand, exclusion, uncertainty, or plot-family change that affects interpretation; obtain missing evidence rather than inventing it. Do not silently infer data from a low-resolution figure when accuracy is consequential. Preserve and supply source data and reproducible code when available.

## Route by task

- For design or critique, read [academic design context](references/design-evidence/design-context.md) to identify the reader's task, intended comparison and tradeoffs. Use the linked source registers to distinguish research findings, editorial requirements and design synthesis; do not load all sources for routine work.
- For a quantitative or conceptual figure, read [figures](references/figures.md).
- For a table, read [tables](references/tables.md).
- For a destination change, submission formatting, or uncertain journal rules, read [journal switching](references/journal-switching.md).
- For critique, refinement, and the final review of a newly created artifact, read [critique](references/critique.md). Creation is not complete at the first valid render. Combine references when the task spans modes.

For a new design with more than one plausible structure, use a small comparison before polishing:

1. Turn the reader's task into two concrete questions that the artifact must answer. Identify which values or observations belong together and what aggregation could hide.
2. Make two rough, content-complete structural candidates in the working files. Change how the evidence can be compared: arrangement of rows/columns, grouping/faceting, or representation of observations and their relationships. Different colors or fonts are not different structures. Use the same evidence and delivery size; do not make the alternative deliberately weak.
3. Inspect the candidates and answer both questions from each. Locate the relevant cells/marks and note any avoidable search, legend decoding, lost variation, or broken relationships. Also inspect the cost: crowding, repeated context, greater size, or a harder secondary comparison. These are design judgments, not measured reader-performance scores.
4. Polish the candidate that best serves the questions while retaining needed evidence. Keep a brief choice and tradeoff in existing code comments or the final handoff. Deliver only the selected artifact unless alternatives were requested.

Keep this bounded to two structures and one correction pass, not a gallery of chart types. Retain a conventional representation when it wins the comparison. For cosmetic edits or a user-fixed structure, preserve it and improve within the given constraints; do not restart structural exploration.

For refinement, retain evidence and intended message while fixing observed problems. For conversion, compare source and output evidence and document intentional changes. For critique, distinguish observed issues from uncertainties and propose concrete fixes.

## Checks and delivery

1. **Integrity blockers:** stop or mark the affected result provisional if evidence is missing, misrepresented, or cannot be preserved. This includes ambiguous uncertainty, denominators, units, mappings or exclusions when needed to interpret the result. Resolve before making a factual claim.
2. **Applicable requirements and defaults:** apply current, authoritative, destination- and stage-specific requirements. Surface conflicts and unknowns; do not merge contradictory rules or call an unverified requirement satisfied. Apply broader style defaults only where applicable and subordinate to specific requirements. If a user chooses a noncompliant draft, identify the deviation.
3. **Academic communication:** assess whether the representation, precision, hierarchy and annotations help the reader perform the intended comparison at the delivered size. A correct table can still make the central comparison unnecessarily difficult. Explain that specific difficulty rather than calling an alternative style inherently wrong. Preserve useful structure and valid alternative designs; visual simplicity is not an end in itself.

Use the reader walkthrough in the critique reference on the rendered artifact at delivery size. Carry a concrete finding through one correction pass and verify the changed location, including any affected caption or note. A choice between two layouts does not replace this review of the selected layout. Preserve a sound design when no consequential issue is found; do not invent a defect to justify revision. If rendering is unavailable, state the limit.

Check actual font appearance, glyphs and labels after export; a declared font or a nominal size does not establish legibility. If a known, fixable rendering defect prevents the requested use, make a bounded correction instead of merely adding a disclaimer. When critiquing, cross-check each allegation against the source and visible content, including titles and notes, before proposing changes.

Deliver the requested editable and export formats as available. Briefly state meaningful design decisions, evidence or formatting changes, actual checks performed, unresolved requirements and any limitations. Profile validation or a metadata comparison alone does not establish journal compliance.

The material/composition separation and bounded iteration are independently adapted from [Hallmark](https://github.com/Nutlope/hallmark/blob/main/skills/hallmark/SKILL.md).
