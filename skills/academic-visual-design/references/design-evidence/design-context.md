# Academic design context

This is a decision reference, not a universal house style. Sources and limits are recorded in [root-sources.json](root-sources.json); table and figure references provide more specific evidence. Source IDs distinguish research findings from editorial guidance. The decision procedure and disciplinary applications below are our synthesis, not experimentally validated rules.

## Define what the reader must do

Use the working brief from [research ingestion](../research-context.md), when applicable, rather than building a second inventory. Before styling, resolve the following design decisions from that context:

- **Reader and use:** specialist reviewer, cross-disciplinary scientist, clinician, student; manuscript, supplement, presentation or exploratory analysis.
- **Scientific object:** observations, estimates, model predictions, image evidence or a conceptual explanation; the estimand and unit of analysis where applicable.
- **Reader task:** retrieve a value; compare models or groups; inspect a distribution; trace change within people; examine uncertainty; follow a mechanism.
- **Primary comparison:** exactly which entries, marks or panels should be read together, and which context must remain visible.
- **Evidence constraints:** units, measurement resolution, precision, sample sizes, denominators, dependence, missingness, transformations and uncertainty identity.
- **Delivery constraints:** actual size, editable format, article/asset type, exact venue and stage; accessible reading alternatives.

Infer ordinary design choices when the request gives enough context. Ask for missing evidence when it changes the scientific meaning; do not ask users to complete a long design questionnaire. A vague instruction such as 'make this publication-ready' is not evidence for a particular journal, font size or statistical convention.

## Principles with bounded support

**Task before visual fashion.** Kim and Heer tested 12 encodings and four tasks with 1,920 participants; effectiveness varied with the task and data distribution. Their study supports conditional encoding choices, not a universal ranking of every scholarly display [R03]. Consider exact retrieval separately from pattern or aggregate comparison.

**Reduce the work of comparison.** The Franconeri review links grouping, attention and working-memory demands to comprehension, while reporting mixed evidence for blanket decluttering. Its emphasis is communication to nonspecialists, not validation of every expert journal convention [R01]. Treat a useful rule, reference line or redundant label differently from decoration. Check the associated correction when using its examples [R02].

**Make visual hierarchy express scientific structure.** A conceptual illustration should distinguish the main mechanism, context and uncertainty; define arrows and symbols rather than decorate a list with icons. Nature's conceptual guide is written for commissioned explanatory figures, not quantitative-data formatting in general [R04]. For quantitative work, highlighting must not manufacture evidential certainty or hide contrary results.

**Design the delivered object, not the editor view.** Check actual text, strokes, symbols and notes at the intended output size. Font declarations alone do not establish successful rendering. Nature's production guide illustrates how narrow the applicable typography and editability requirements can be; its numeric bounds and gridline preferences are not general design laws [R05].

**Accessibility includes structure and meaning.** SIGCHI guidance asks for real tables with identified headers, redundant distinguishing cues, and figure descriptions that complement captions. Check exported structure as well as visible pixels; native authoring does not automatically guarantee an accessible PDF [R06]. Treat exact venue requirements separately from the wider goal of making evidence available to readers who cannot perceive the image.

## Design moves and their reversal conditions

| Design move | Use when | Reverse or adapt when |
|---|---|---|
| Round displayed values | Extra digits obstruct the intended comparison and exceed useful precision | Small meaningful effects, thresholds or measurement resolution would disappear; change units explicitly or retain digits |
| Put models across columns | The reader compares the same coefficient across a manageable set of specifications | Many models, long labels or multiple model statistics make row-based lookup clearer |
| Use a compact table | The reader needs exact estimates, heterogeneous units or several statistics | Distribution, trajectory or relationship is the real question; a numerical grid hides it |
| Show observations or connected pairs | Individual variation or within-unit change is scientifically relevant | Raw observations are unavailable, privacy restricts disclosure, or overplotting defeats inspection; use honest summaries rather than invented dots |
| Use aligned points and intervals | Comparing estimates and their supplied uncertainty is central | The task is composition, distribution shape, topology or an explicitly categorical workflow |
| Directly label series | Few series and clear space reduce mapping effort | Labels collide or dense panels repeat the same mapping; use a stable, nearby key or facets |
| Align panel scales | Cross-panel magnitude comparison is intended and units match | Different units or a clearly disclosed within-panel question require separate scales |
| Simplify rules, colors or decoration | They compete with evidence or imply groups that do not exist | Their removal makes row tracking, category identification or reference comparison harder |

Row/column comparison direction, portrait/landscape page orientation, and rotated text are separate decisions. These are synthesis rules. Test the reversal condition before treating a preference as a defect. An attractive table can be scientifically wrong; a dense table can be appropriate for a specialist appendix.

## Disciplinary use cases

These are task-specific applications, not a mandate that every field use one design.

| Research context | Reader's likely question | Useful design direction | Common failure to inspect |
|---|---|---|---|
| APA / behavioral research | How do groups, associations or model estimates differ? | Distinguishable descriptive quantities; coefficients and uncertainty; paired observations when the design is paired | Means conceal distributions; SD/SE/CI confused; unexplained reference groups |
| JAMA / clinical research | What outcome occurred, in whom, with what uncertainty? | Explicit denominators, time horizon and absolute/relative effect identity; compact outcomes tables and appropriately annotated effect/survival plots | Percentages without their population; sparse follow-up hidden; clinical importance inferred from stars |
| AER / economics | How does the estimand change across specifications? | Model identity, coefficient/uncertainty association, sample and specification metadata; event-time or coefficient comparisons when appropriate | Table orientation defeats specification comparison; omitted-category or clustered-SE notes disappear |
| IEEE / engineering | What performance tradeoff holds under comparable conditions? | Units and metric direction, comparable workloads, quality/resource tradeoffs, distributions across runs when available | A single best run treated as robust evidence; incomparable conditions; too many metrics on one scale |
| ACM / computing and HCI | Which system or intervention works for this task and population? | Declared metrics, conditions, aggregation and run/participant identity; ablation structure; semantic table headers | Best-cell bolding mistaken for statistical separation; weighted averages obscure subgroup behavior |
| Nature / multidisciplinary science | What is the principal result and how does each panel support it? | Coherent panel reading order and stable encodings; distinguish raw images, summaries and mechanisms | Overpacked panels; unlabeled image scales; visual emphasis outruns evidence |

The actual data and reader task take precedence over these associations. Consult the exact destination profile for compliance; examples of published typesetting are not automatically author-submission rules.

## Critique and acceptance

Assess three distinct outcomes: scientific integrity, applicable destination requirements, and academic communication quality. Do not average away a scientific error with attractive typography. For each proposed design correction, identify the affected reader task and concrete location; check that the allegation agrees with visible text and source evidence. Conditional advice is not an observed blocker.

A useful comparison asks whether a reader can find the requested estimate, identify its uncertainty and denominator, compare the intended entries, and recognize qualifications without reconstructing the layout. Use blind A/B/tie judgments with reasons tied to those tasks. Model preferences are not measured human reading speed or expert consensus. Preserve valid alternative designs and cases where the simpler-looking option loses information.

For creation or revision, keep a short decision record in the work: intended comparison; chosen representation; one important tradeoff; evidence/format changes; actual rendered checks. Do not turn that internal reasoning into unnecessary subtitles or explanatory copy in the artifact.

## Visual examples

The accompanying original synthetic casebook illustrates these decisions. It is teaching material, not a new benchmark or evidence that a design is universally superior. Its precision counterexample intentionally includes a lossy display and identifies it as such; full source values remain available. Published exemplars are linked in the source records rather than copied into the skill.
