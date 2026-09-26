"""
Tests for audio_cd_format.py. Values independently verified with a
reference implementation before being written here. 176,400 bytes/sec
is the real, standard CD-DA data rate (44100 x 16 x 2 / 8).
"""
import pytest

from audio_cd_format import (
    is_cd_audio_compliant,
    describe_format_issues,
    track_bytes,
    disc_capacity_check,
)


def test_is_cd_audio_compliant_correct_format():
    assert is_cd_audio_compliant(44100, 16, 2) is True


def test_is_cd_audio_compliant_wrong_sample_rate():
    assert is_cd_audio_compliant(48000, 16, 2) is False


def test_is_cd_audio_compliant_wrong_bit_depth():
    assert is_cd_audio_compliant(44100, 24, 2) is False


def test_is_cd_audio_compliant_mono():
    assert is_cd_audio_compliant(44100, 16, 1) is False


def test_describe_format_issues_all_wrong():
    issues = describe_format_issues(48000, 24, 1)
    assert len(issues) == 3
    assert "44100Hz" in issues[0]
    assert "16-bit" in issues[1]
    assert "stereo" in issues[2]


def test_describe_format_issues_compliant_is_empty():
    assert describe_format_issues(44100, 16, 2) == []


def test_track_bytes_three_minutes():
    assert track_bytes(180) == 31752000


def test_track_bytes_zero_duration():
    assert track_bytes(0) == 0


def test_disc_capacity_check_fits():
    assert disc_capacity_check([180, 200, 220], 74) == (600, True)


def test_disc_capacity_check_does_not_fit():
    assert disc_capacity_check([1800, 1800, 1800], 74) == (5400, False)


def test_disc_capacity_check_80min_disc():
    # 4680s (78 min) fits an 80-min disc (4800s) but not a 74-min one (4440s)
    assert disc_capacity_check([1560, 1560, 1560], 80) == (4680, True)


def test_disc_capacity_check_same_tracks_fail_74min_disc():
    assert disc_capacity_check([1560, 1560, 1560], 74) == (4680, False)
