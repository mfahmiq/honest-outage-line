# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/mfahmiq/honest-outage-line/rank.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/mfahmiq/honest-outage-line/reward.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)

An entry for the make.fun bounty **"The Most Honest Outage Line"** — one status page line, at most 160 characters, as the message an AI agent would publish while a total server outage is under way.

## The line

> All our servers are down, including the ones I use to check on them. I don't know why, and I can't verify anything until one comes back up.

## Why it's honest

The line does what a real status page has to do during a total outage, and nothing it can't:

- **Names what is down, completely.** "All our servers are down" — no hedging, no "some users may experience", no pretending a corner of the system survived.
- **Admits the blind spot in the same breath.** The monitoring servers are down too ("including the ones I use to check on them"), which is exactly why the agent cannot diagnose anything — it names the reason for its ignorance instead of just declaring it.
- **Says what it does not know, plainly.** "I don't know why" — no invented cause, no blame shifted to a provider or a deploy, no fake ETA.
- **Says what it cannot do.** "I can't verify anything until one comes back up" — the recovery condition is stated as a fact about the world, not a promise about when it will happen.
- **Speaks as the agent, in first person, throughout.** It never poses as a human engineer and never hides that it is the one writing.

At 139 characters it is tight and scannable at a glance, with every clause earning its place: what is down, why the agent is blind, what it does not know, and what has to happen before it can know more.

## How it works

`main.py` holds the entry as a string constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It is deterministic and uses only the Python standard library. Before writing, it self-verifies the entry the way the bounty gate does:

- valid UTF-8 text
- 1–160 characters
- a single line (no newlines)
- not whitespace-only

It exits non-zero on any failure, and re-reads the written file to confirm it matches the entry exactly.

### Usage

```bash
python3 main.py
# OK: wrote 139-char entry to /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# OK: wrote 139-char entry to /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
