# ResDes

An agent skill for designing and refining academic figures and tables while preserving scientific meaning.

## Install

Clone this repository and copy [`skills/academic-visual-design`](skills/academic-visual-design) into your agent's skills directory. For Codex, use `~/.codex/skills/`.

## Use

> Use $academic-visual-design to improve this figure and table. Read the manuscript and analysis outputs first, preserve the results, and return editable sources and exports.

Supports figure and table design, critique, research-context ingestion, and journal-format changes. Includes design references, synthetic examples, and partial journal profiles.

Experimental. Review outputs before publication; journal requirements need current verification. Visual review can still miss caption-to-marker mismatches.

## Evaluation

The skill explicitly preserves useful structure during journal changes and requires viewing final native exports, with reinspection after repairs. In a controlled Word test, an unprompted reviewer found an invisible value, repaired its formatting, and viewed the final export without changing the table data. Both v8 and v9 completed native inspection in a matched test with clarified tooling; this does not establish a v9-specific advantage or general design reliability. See the [test results and limitations](evaluations/native-review/results.json) and [rendered before/after](evaluations/native-review/before-after.png).

## Development

Python 3 is required for the profile utility and its tests:

```sh
python -m unittest discover -s skills/academic-visual-design/scripts -p "test_*.py"
```

Regenerating the synthetic casebook additionally requires Matplotlib and NumPy. Sources and attribution are retained alongside the skill. No license has been selected yet.
