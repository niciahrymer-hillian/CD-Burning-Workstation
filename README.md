# CD-Burning-Workstation

### Turning the repurposed Linux machine into a burn station: buying the right blank media, pulling audio from YouTube, and cutting real Audio CDs.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[📖 Lesson Plan](docs/LESSON_PLAN.md)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

> ⬜ **Scaffold pending.** Directory created to portfolio standard; full content (README, lesson plan,
> tour + quiz, skeleton code) still to be built. Part of **Chain K — Hardware & Systems Foundations**.

## Why This Was Built

The old machine from **Linux-On-Old-Hardware** is sitting there with a working Linux install and
(usually) an optical drive nobody uses anymore — a genuinely satisfying project is putting it to work
as a dedicated burn station: archiving favorite YouTube tracks, podcasts, and lectures as real Audio
CDs that play in a car with no Bluetooth, an old boombox, or any CD player, with zero dependency on
streaming, an account, or an internet connection ever again.

It's also the natural next place to actually *use* the shell fluency from **Shell-And-Small-Software**
instead of just drilling it — wrapping `yt-dlp` and `ffmpeg` in a real script with argument validation
and exit codes is the exact skill that project practices, applied to something tangible.

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

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
