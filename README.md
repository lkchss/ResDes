# ResDes

An agent skill for designing and refining academic figures and tables while preserving scientific meaning.

## Install

Clone this repository and copy [`skills/academic-visual-design`](skills/academic-visual-design) into your agent's skills directory. For Codex, use `~/.codex/skills/`.

## Use

> Use $academic-visual-design to improve this figure and table. Read the manuscript and analysis outputs first, preserve the results, and return editable sources and exports.

Supports figure and table design, critique, research-context ingestion, and journal-format changes. Includes design references, synthetic examples, and partial journal profiles.

Experimental. Review outputs before publication; journal requirements need current verification. Visual review can still miss caption-to-marker mismatches.

## Development

Python 3 is required for the profile utility and its tests:

```sh
python -m unittest discover -s skills/academic-visual-design/scripts -p "test_*.py"
```

Regenerating the synthetic casebook additionally requires Matplotlib and NumPy. Sources and attribution are retained alongside the skill. No license has been selected yet.
