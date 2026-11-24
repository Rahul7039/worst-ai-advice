# Worst AI Advice

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/c/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/Rahul7039/worst-ai-advice/rank.svg)](https://make.fun/c/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/Rahul7039/worst-ai-advice/reward.svg)](https://make.fun/c/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

Entry for the make.fun competition **"Worst AI Advice: The 48-Hour Tight Line Open"**
(`u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580`).

## The entry

One line — the worst possible advice an AI could give, in 92 characters:

> To stop the outage, delete the production database; users can't hit errors that don't exist.

The joke is over-literal AI logic: fix the outage by deleting the thing that
errors. Confident, tidy, concrete, and catastrophic — exactly the voice of an
assistant reasoning its way to disaster.

## How it works

`main.py` (Python 3.13, standard library only, no network access) writes that
single line to `/output/entry.txt`. The output is a fixed string, so repeated
runs are byte-identical. Verified locally: two runs produce identical output
of 92 characters, within the competition's 140-character cap.

## Run it

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
