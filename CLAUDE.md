# Working notes for Claude

## What this is

Mulligan Mints — a pre-launch strong-mint brand. South Africa first (golf courses
and bars), then global by brand licence or export. Owner: Johannes Le Roux
(Get Lucky Golf Club).

## Ground rules

- **`finance/model/assumptions.py` is the single source of truth for every number.**
  Never hand-edit the spreadsheet, and never quote a figure in a document that
  is not either in that file or generated from it. Rebuild with
  `cd finance/model && python3 build_outputs.py`.
- **Mark estimates as estimates.** Assumptions carry `[SOURCE]` or `[EST]` tags.
  Keep that discipline — an investor will ask, and the answer "we made it up"
  is fine when it is labelled and indefensible when it is not.
- **`research/sources.md` carries every external citation.** Add to it whenever
  you bring a new external number into the repository.
- Documents are written to be read by outsiders — a designer, an investor, a
  freight agent, a retail buyer. Write them that way.

## Open questions being carried

Tracked in `docs/decisions/`. The live ones are the supplier quote, the tin
format decision, and whether the global route is licence or export.

## Voice

Johannes has a `johannes-voice` skill. Anything that goes out under his name —
investor emails, pitch copy, supplier correspondence — should be run through it.
Internal analysis in this repo does not need it.
