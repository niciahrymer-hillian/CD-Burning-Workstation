"""
Audio CD Format -- fill in the four functions below.

The real Red Book Audio CD compliance and capacity math behind the
Format & Capacity Simulator tab: why "any audio file" doesn't burn a
disc that plays reliably, and why a disc's real capacity is measured
in time, not megabytes, once you know the actual data rate.

Run the tests as you go:  pytest exercises/test_audio_cd_format.py -v
All four start failing. Implement one function, re-run, watch it turn
green, move to the next.
"""


def is_cd_audio_compliant(sample_rate_hz, bit_depth, channels):
    """Audio CD (Red Book / CD-DA) requires EXACTLY 44100Hz, 16-bit,
    2-channel (stereo) PCM audio -- not "close enough," not "a format
    my player also happens to support." This checks a track's raw
    format against those three fixed requirements.

    >>> is_cd_audio_compliant(44100, 16, 2)
    True
    >>> is_cd_audio_compliant(48000, 16, 2)
    False
    """
    # TODO: return sample_rate_hz == 44100 and bit_depth == 16 and channels == 2
    raise NotImplementedError


def describe_format_issues(sample_rate_hz, bit_depth, channels):
    """A real diagnostic: which specific requirement(s) a track fails,
    in plain language -- the actual output a conversion script should
    show you before you waste a blank disc on a track that was never
    going to burn correctly.

    >>> describe_format_issues(48000, 24, 1)
    ['sample rate 48000Hz — Audio CD requires exactly 44100Hz', 'bit depth 24-bit — Audio CD requires exactly 16-bit', '1 channel(s) — Audio CD requires exactly 2 (stereo)']
    """
    # TODO: build a list; append a message for each of sample_rate_hz,
    # bit_depth, and channels that doesn't match the Audio CD requirement
    # (44100 / 16 / 2 respectively). Return the list (empty if compliant).
    raise NotImplementedError


def track_bytes(duration_seconds):
    """How many raw bytes a track actually occupies on the disc, given
    its duration. Audio CD's fixed data rate is 176,400 bytes/second
    (44,100 samples/sec x 16 bits x 2 channels / 8 bits-per-byte) --
    every compliant track uses exactly this rate, which is also why
    disc capacity is really a time budget, not a simple size budget.

    >>> track_bytes(180)
    31752000
    """
    # TODO: return duration_seconds * 176400
    raise NotImplementedError


def disc_capacity_check(track_durations_seconds, disc_minutes=74):
    """Given a list of track durations (seconds) and a disc's rated
    capacity in minutes (74 or 80 are the two real Audio CD sizes),
    return (total_seconds_used, fits) -- whether the whole track list
    actually fits on that disc.

    >>> disc_capacity_check([180, 200, 220], 74)
    (600, True)
    >>> disc_capacity_check([1800, 1800, 1800], 74)
    (5400, False)
    """
    # TODO: total = sum(track_durations_seconds); capacity = disc_minutes * 60
    # return (total, total <= capacity)
    raise NotImplementedError
