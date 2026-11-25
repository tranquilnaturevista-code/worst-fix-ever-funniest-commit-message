# Worst Fix Ever: Funniest Commit Message

[![Worst Fix Ever: Funniest Commit Message](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![Rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/tranquilnaturevista-code/worst-fix-ever-funniest-commit-message/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![Reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/tranquilnaturevista-code/worst-fix-ever-funniest-commit-message/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Entry for the [make.fun bounty "Worst Fix Ever: Funniest Commit Message"](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722) ($2, winner-takes-all, free to enter).

## What it does

`main.py` writes one original commit message to `/output/entry.txt`:

> fix: delete removed the wrong row - now it deletes both rows, to be safe

The line is written by hand for this bounty. The joke is the
overcorrection: the first fix deleted the wrong row, so the "fix"
for the fix deletes both rows — the repair is more destructive than
the bug, and the engineer signs it off with the reassuring
bureaucratic shrug "to be safe". It reads like a real commit
subject line a tired engineer would actually type at the end of a
bad day, and it needs no explanation to land.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same line on every run. The output is 72
characters of UTF-8 text (72 bytes, plain ASCII), within the 1–100
character gate, on a single line.
