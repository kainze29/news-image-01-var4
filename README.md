# news-image-01 var4: Friday 13 November 2026 as a breaking-news timeline

One image that sums up the world's news of Friday 13 November 2026,
told the way a TV newsroom tells a day: a red BREAKING banner, then
the six most consequential stories in the order they unfolded, each
with a time-of-day stamp and a one-line headline.

| When | Story |
| --- | --- |
| EARLY | NVIDIA CEO RESIGNS: Nvidia chief Jensen Huang resigns; shares fall about 16%; the US Senate Banking Committee had summoned Huang and Commerce Secretary Lutnick |
| MORNING | UKRAINE TALKS: Zelensky meets US envoys; Europe is promised a seat at the next round of Ukraine-Russia talks; a large prisoner exchange is agreed |
| MIDDAY | DRONE STRIKES RUSSIAN WARSHIP: a Ukrainian drone strikes the Russian corvette Naro-Fominsk in the Gulf of Finland; Finland confirms detecting the strike |
| AFTERNOON | IRAN CLAIMS BAHRAIN STRIKE: Iran says it struck a US radar site in Bahrain as Gulf tensions rise |
| EVENING | FBI: N. KOREA $400M HACK: the FBI says North Korean hackers used fake video calls and deepfakes to steal about $400m in crypto |
| NIGHT | STRIKE HITS GAZA HOSPITAL: an Israeli strike on Nasser Hospital in Khan Younis kills six people, including a surgeon |

The day-part stamps (EARLY through NIGHT) order the stories as the
day unfolded; they are not clock times. Every fact above is a story
first reported on 13 November 2026.

## How it runs

`main.py` (Python 3, standard library only) checks that the bundled
`news.png` is a genuine 1024x1024 PNG, then copies it byte-for-byte
to `/output/entry.png` and verifies the copy is the same size. No
network, no rendering, so every run writes identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program
- `news.png` — the timeline image (1024x1024 PNG, under 1 MiB)
- `LICENSE` — MIT
