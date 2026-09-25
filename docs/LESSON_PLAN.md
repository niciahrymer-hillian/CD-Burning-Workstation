# 📖 Lesson Plan — CD-Burning-Workstation

> **Chain K — Hardware & Systems Foundations** | Turning the repurposed Linux machine into a burn
> station: buying the right blank media, pulling audio from YouTube, and cutting real Audio CDs.

## What This Project Is

Put the machine from Linux-On-Old-Hardware to work as a dedicated CD-burning station: choose the right
blank media, pull audio down cleanly, convert it to a format an actual Audio CD requires, burn it, and
verify the disc actually works — all wrapped in a script that applies what Shell-And-Small-Software
practiced.

## Learning Objectives

By the end I can:

1. Choose the right blank CD type, capacity, and write speed for the drive and the burn's purpose.
2. Download and convert YouTube audio to a clean, CD-compliant format with `yt-dlp` and `ffmpeg`.
3. Build a track order and burn a standards-compliant Audio CD (plays in any CD player), versus a Data
   CD (files, e.g. MP3s, in a filesystem).
4. Verify a burn actually completed correctly before trusting it.
5. Wrap the whole pipeline (download → convert → burn) in a script with real argument validation and
   exit codes.
6. Recognize where personal-use archival ends and something you shouldn't be downloading begins.

## Software You Will Use

- `yt-dlp` (actively maintained, for personal-archival downloads).
- `ffmpeg` / `ffprobe` (audio conversion and format verification).
- `wodim` or `cdrecord` (burning); `cdrskin` as a modern alternative.
- `genisoimage`/`mkisofs` (if building a Data CD instead of an Audio CD).
- Optional GUI: Brasero or K3B.

## Build Order

1. Confirm the old PC's optical drive can burn, not just read — check with `wodim --devices` or
   `dmesg` after inserting a blank disc.
2. Install `yt-dlp` and `ffmpeg`; download one track and inspect the output format with `ffprobe`.
3. Convert it to 44.1kHz/16-bit stereo PCM WAV — the exact format Audio CD requires — and confirm.
4. Burn a short test disc (2-3 tracks) as an Audio CD; play it back in a real CD player to confirm
   compatibility, not just that the burn "completed."
5. Script the pipeline: given a list of URLs, download, convert, order, and burn — with argument
   validation and clear exit codes.
6. Burn a full-length real disc and verify it (read-back / checksum) before relying on it.

## Common Mistakes to Avoid

- Burning straight from a downloaded MP3/AAC without converting to the exact PCM format Audio CD
  needs — some burners "accept" it but produce a disc that skips or won't play in older players.
- Buying the cheapest unbranded CD-R spindle for something meant to last — dye quality affects both
  burn reliability and long-term readability.
- Assuming every optical drive can burn — plenty are read-only, especially in a machine repurposed as
  "just a Linux box."
- Not verifying the burn — a disc that appears to finish can still contain read errors.
- Downloading and redistributing copyrighted content. This project is for personal-use archival of your
  own material or content you have the rights to, not piracy.

## Check Your Understanding

The quiz covers Audio CD format requirements, CD-R vs CD-RW/capacity tradeoffs, when to use
`wodim`/`cdrecord` versus `mkisofs`, and why burn verification matters.

## Why This Matters (Industry Application)

Chaining CLI tools into one repeatable, validated pipeline — fetch, transform to a required format,
load into a fixed target — is a small-scale version of any real ETL pipeline. Understanding *why* Audio
CD requires exactly 44.1kHz/16-bit stereo PCM, not "any audio file," is the same format-compliance
thinking that matters far beyond optical media.

## Reflection Questions

- What's actually gained by burning a physical disc in 2026 versus keeping a folder of files or just
  streaming?
- Where's the line, for you, between personal archival and something you shouldn't be downloading at
  all?
