"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

import pytest

from scoring import session_rating


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"


def test_session_rating_boundary_59_is_skip():
    assert session_rating(59) == "Skip"


def test_session_rating_boundary_80_is_good():
    assert session_rating(80) == "Good"

def test_session_rating_boundary_60_is_meh():
    assert session_rating(60) == "Meh"


# Part 3: breaker inputs. Out of range is rejected; a decimal inside the
# range is valid input and still rates normally.
def test_session_rating_rejects_negative():
    with pytest.raises(ValueError):
        session_rating(-1)


def test_session_rating_rejects_over_100():
    with pytest.raises(ValueError):
        session_rating(150)


def test_session_rating_rejects_non_number():
    with pytest.raises(TypeError):
        session_rating("90")


def test_session_rating_accepts_decimal():
    assert session_rating(87.5) == "Good"