# Flashcards — Bayesian Spine spaced-repetition deck

A tab-separated Anki deck (`deck.tsv`, 164 cards) drilling the retrieval-worthy numbers, formulas, and judgment calls from the 27-module course — one field of canonical numbers verified against `../modules/SPINE-INDEX.md`.

**Import into Anki:** File → Import → select `deck.tsv`. Set field separator to **Tab**, map Field 1 → Front, Field 2 → Back, Field 3 → Tags, and check **Allow HTML in fields** (backs use `<br>` and MathJax `\( … \)`).

**Tag scheme:** each card's tag field is `<module-id> <topic>` (e.g. `M05 conjugacy`), which Anki reads as two tags — filter by module (`M05`) or by theme (`conjugacy`, `hmc`, `causal`).

**Study cards only AFTER reading the module.** Every front is a retrieval prompt whose answer is unrecoverable — and often actively misleading to guess — without having worked through that module first. The deck reinforces understanding; it does not create it.
