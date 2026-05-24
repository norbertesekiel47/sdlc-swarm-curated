"""Tests for string_utils module."""
from src.string_utils import reverse_string, is_palindrome, is_anagram


def test_reverse():
    assert reverse_string("hello") == "olleh"


def test_palindrome():
    assert is_palindrome("racecar") is True


def test_anagram():
    assert is_anagram("listen", "silent") is True
