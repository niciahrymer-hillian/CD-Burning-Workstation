# Exercises — Audio CD Format

A hands-on companion to Lessons 2 and 3 in the interactive tour: the real Red Book Audio CD compliance
and capacity math behind the Format & Capacity Simulator tab — why "any audio file" doesn't reliably
burn, and why disc capacity is really a time budget once you know the real data rate.

## Setup

```bash
# from this exercises/ folder
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest
```

## Run the tests

```bash
pytest -v
```

You'll see 11 failing tests — every function in `audio_cd_format.py` currently raises
`NotImplementedError`.

## What to do

Open `audio_cd_format.py`. Implement in this order:

1. `is_cd_audio_compliant` — the three fixed requirements: 44100Hz, 16-bit, stereo.
2. `describe_format_issues` — a real diagnostic listing exactly what's wrong, if anything.
3. `track_bytes` — the actual data-rate math: 176,400 bytes/second for compliant audio.
4. `disc_capacity_check` — whether a track list actually fits a 74 or 80-minute disc.

## When you're done

All 11 tests passing means you have the same compliance and capacity logic real burning software
(Brasero, K3B) runs before it ever touches a blank disc — worth having as functions if you're
scripting the whole download-convert-burn pipeline instead of clicking through a GUI each time.
