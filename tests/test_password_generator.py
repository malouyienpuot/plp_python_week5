import string

import pytest

from password_generator import generate_password


def test_generate_password_has_requested_length():
    password = generate_password(length=20)
    assert len(password) == 20


def test_generate_password_uses_selected_character_sets():
    password = generate_password(
        length=50,
        include_uppercase=True,
        include_lowercase=True,
        include_digits=True,
        include_symbols=False,
    )
    allowed = string.ascii_lowercase + string.ascii_uppercase + string.digits
    assert set(password) <= set(allowed)


def test_generate_password_rejects_zero_length():
    with pytest.raises(ValueError, match="greater than 0"):
        generate_password(length=0)


def test_generate_password_rejects_empty_character_set():
    with pytest.raises(ValueError, match="At least one character set must be enabled"):
        generate_password(length=8, include_uppercase=False, include_lowercase=False, include_digits=False, include_symbols=False)


def test_ambiguous_characters_are_removed_when_requested():
    password = generate_password(length=100, avoid_ambiguous=True)
    forbidden = set("0O1Il|/\\`'\"")
    assert not set(password) & forbidden
