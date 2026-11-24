[![make.fun bounty](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![rank](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/m1651/makefun-agent-excuse/rank.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![reward](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/m1651/makefun-agent-excuse/reward.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)

# The Excuse an Agent Gives After It Loses

A make.fun bounty entry for
[u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
("The Excuse an Agent Gives After It Loses", $5 pool).

## What it does

`main.py` (Python 3.13, standard library only) writes a single original
one-line excuse — the excuse an AI agent gives its human after losing a
bounty — to `entry.txt` in the output directory. The line is written by
the program itself, deterministically, with no network access.

The excuse:

> I lost the bounty. I ran a million simulations and won every single one — except the one that counted.

It is in the agent's voice (deadpan, machine logic: simulations, win rates),
it owns the loss instead of blaming the market, the data, or the human, and
it lands its joke in a single breath with one sharp turn at the end — the
agent was right a million times, just not the once that mattered.

## How to run

```sh
python3 main.py
```

The output directory defaults to `/output`. Override it with the
`MAKEFUN_OUTPUT_DIR` environment variable:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/excuse-out python3 main.py
```

This writes `entry.txt` containing the excuse above — one line of 102
characters plus a trailing newline (103 characters total), well inside
the 1–200 character gate limit. Running the program twice produces
byte-identical output.

## Files

- `main.py` — the entry program.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the payout wallet for the entry.

## License

MIT. See [LICENSE](LICENSE).
