# CD-Burning-Workstation

### Turning the repurposed Linux machine into a burn station: buying the right blank media, pulling audio from YouTube, and cutting real Audio CDs.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[🎮 Interactive Tour](docs/interactive/index.html) · [📋 Cheat Sheet](docs/CHEATSHEET.pdf) · [📖 Full Lesson](docs/LESSON.pdf) · [🔗 Resources](docs/RESOURCES.pdf) · [📖 Lesson Plan](docs/LESSON_PLAN.md)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

Part of **Chain K — Hardware & Systems Foundations**. Depends on **Linux-On-Old-Hardware** for the
machine itself and its optical drive, and on **Shell-And-Small-Software** for the scripting fluency
this project applies directly.

## What this is

The old machine from **Linux-On-Old-Hardware** is sitting there with a working Linux install and
(usually) an optical drive nobody uses anymore — a genuinely satisfying project is putting it to work
as a dedicated burn station: archiving favorite YouTube tracks, podcasts, and lectures as real Audio
CDs that play in a car with no Bluetooth, an old boombox, or any CD player, with zero dependency on
streaming, an account, or an internet connection ever again. It's also the natural next place to
actually *use* the shell fluency from **Shell-And-Small-Software** instead of just drilling it. The
four lessons build in the order a real burn actually needs them: pick the right blank media and confirm
the drive can burn, download and convert audio to the exact format Audio CD requires, burn and verify
it properly, then wrap the whole pipeline in a validated script. Check real Audio CD format compliance
and budget a real disc's time capacity in the **Format & Capacity Simulator** tab before you burn a
disc that skips, or doesn't fit at all.

**Distro compatibility note**: every tool this project uses — `yt-dlp`, `ffmpeg`, and
`wodim`/`genisoimage` (bundled as the `cdrkit` package) — installs natively on whichever lightweight
distro Linux-On-Old-Hardware ended up choosing: `apt` on Debian/Xubuntu, `apk` on Alpine. Same tools,
different package manager, not a compatibility gap. The one thing to actually watch for is optional GUI
burners (Brasero/K3B) — both pull in a real slice of GNOME's or KDE's library stack, which conflicts
with a machine chosen specifically for a lightweight desktop (or no desktop at all, on Alpine). The CLI
tools this project centers on are the actual recommended path here, not just the "advanced" option.

## Prerequisites

| Requirement | Notes |
|---|---|
| A modern browser | Chrome, Firefox, Safari, or Edge — the interactive tour is a single HTML file, no install |
| Python 3.8+ (for the exercises) | Check with `python3 --version` |
| The Linux-On-Old-Hardware machine with an optical burner (optional for the tour/exercises) | Only needed for a real build — the tour and exercises need nothing but a browser and Python |

## Items Needed

- [ ] The machine from **Linux-On-Old-Hardware**, with a confirmed-working optical burner (check with `wodim --devices` — see [Hardware Buying Guide](#hardware-buying-guide-what-to-look-for--red-flags) below)
- [ ] Blank CD-R media (CD-RW only if you specifically need rewritability — many players can't read CD-RW)
- [ ] `yt-dlp`, `ffmpeg`, and `wodim`/`genisoimage` (`cdrkit`), installed via your distro's package manager
- [ ] Nothing else required for the tour or exercises — just a browser and Python

## Quick Start

1. **Open the interactive tour.** Double-click `docs/interactive/index.html` — no server, no build step.
2. **Work Lesson 1 (Blank media & drive capability)**, and confirm your drive can actually burn with
   `wodim --devices` before buying any media.
3. **Do the skeleton-code exercise.**
   ```bash
   cd exercises
   python3 -m venv .venv && source .venv/bin/activate
   pip install pytest
   pytest -v
   ```
   You'll see 12 failing tests. Open `exercises/audio_cd_format.py` and implement the four functions —
   full instructions in [`exercises/README.md`](exercises/README.md).
4. **Work Lesson 2 (Acquisition & conversion)**, then open the **Format & Capacity Simulator** tab's
   compliance checker and try a few non-standard sample rates/bit depths/channel counts.
   > ⚠️ **You may get stuck here:** a burner can "accept" a non-compliant file with no error and still
   > produce a disc that skips — always verify format with `ffprobe` before burning, don't trust a
   > successful-looking burn as proof the format was right.
5. **Work Lesson 3 (Burning & verification)**, then add tracks in the Simulator's capacity panel until
   they no longer fit a 74-minute disc.
6. **Work Lesson 4 (Automation & ethics)** and write the validation step of your pipeline script first.
7. **Then the Quiz**, then Flashcards/Match/Pop Quiz for review.
8. **Check the Report Card tab** any time. Click **Print / Save as PDF** to keep a dated copy in `docs/`.

## Exercise Overview

| # | Lesson | Concept | Format & Capacity Simulator tie-in |
|---|---|---|---|
| 1 | Blank media & drive capability | CD-R vs CD-RW, dye quality, burn capability check | *(hands-on check — no simulator panel)* |
| 2 | Acquisition & conversion | Exact Audio CD format requirement | The compliance checker panel |
| 3 | Burning & verification | Audio vs Data CD, TAO/DAO, verification | The disc capacity budget panel |
| 4 | Automation & ethics | Scripting the pipeline, personal-use line | *(design/scripting exercise — no simulator panel)* |

**Learning path:**
```
Lesson 1 (media & drive)  →  Lesson 2 (acquisition & conversion)  →  Lesson 3 (burning & verification)  →  Lesson 4 (automation & ethics)
                                       ↓                                        ↓
                          Format compliance checker              Disc capacity budget
                                       ↓                                        ↓
                                       exercises/ (audio_cd_format.py)
                                                    ↓
                              Quiz → Flashcards/Match/Pop Quiz → Report Card
```

## Hardware Buying Guide (What to look for & red flags)

**Parts list:** blank CD-R media (the only new hardware most builds need), and — only if the
Linux-On-Old-Hardware machine's optical drive turns out to be read-only — an external USB CD/DVD
burner.

**What to look for:** archival-quality CD-R with a stated, reputable dye type; if buying an external
burner, one with clear Linux/`wodim` compatibility rather than a Windows-only bundled-software listing.

**Red flags:** unbranded CD-R spindles with no dye or brand information at all, and "external burner"
listings that turn out to be read-only drives with "burner" used loosely in the title.

**Common failure points:** assuming the machine's existing optical drive can burn without checking
first (many are read-only), and buying the cheapest unbranded media for something meant to last.

Full pricing tiers are in the chain-wide [Hardware Shopping List](../HARDWARE_SHOPPING_LIST.md#cd-burning-workstation).

## Why This Matters (Industry Application)

Chaining together a handful of CLI tools (`yt-dlp` → `ffmpeg` → `wodim`/`cdrecord`) into one repeatable
pipeline — with the right validation and error handling at each stage — is a small-scale version of any
real ETL pipeline: fetch, transform to a required format, load into a fixed target. Understanding *why*
Audio CD requires exactly 44.1kHz/16-bit stereo PCM, not "any audio file," is the same kind of format-
compliance thinking that matters far beyond optical media.

## Topics Covered

| Area | What this project covers |
|------|--------------------------|
| Blank media | CD-R vs CD-RW, capacity (650MB/74min vs 700MB/80min), dye quality, write speed |
| Acquisition | `yt-dlp` — downloading audio from YouTube for personal archival |
| Conversion | `ffmpeg` — re-encoding to CD-Audio-compliant 44.1kHz/16-bit stereo PCM |
| Burning | `wodim`/`cdrecord` for Audio CDs; `genisoimage`/`mkisofs` for Data CDs |
| Verification | Read-after-write checks; confirming real playback compatibility |
| Automation | Scripting the whole download → convert → burn pipeline with real argument validation |
| Ethics | Personal-use archival versus redistribution — where the line actually is |

## How This Connects

Chain K (Hardware & Systems Foundations). Depends on **Linux-On-Old-Hardware** for the machine itself
and its optical drive, and on **Shell-And-Small-Software** for the scripting fluency this project
applies directly — wrapping `yt-dlp`/`ffmpeg`/`wodim` in one validated, error-handled script instead of
typing each command by hand every time.

## Project Layout

```
CD-Burning-Workstation/
├── docs/
│   ├── interactive/index.html   # tour: lessons, quiz, flashcards, match, pop quiz, format/capacity simulator, report card
│   ├── LESSON_PLAN.md           # short build-plan reference
│   ├── LESSON.pdf               # the full written lesson, printable
│   ├── CHEATSHEET.pdf           # one-page recap, printable
│   └── RESOURCES.pdf            # further-reading links, printable
├── exercises/
│   ├── audio_cd_format.py       # skeleton — implement the 4 functions
│   ├── test_audio_cd_format.py
│   └── README.md
└── README.md                    # this file
```

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
