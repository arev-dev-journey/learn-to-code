import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../exercises')))

from strings import count_letter_occurrences, is_palindrome, count_vowels, is_substring

def test_count_letter_occurrences():
    assert count_letter_occurrences("hello", "l") == 2

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False

def test_count_vowels():
    assert count_vowels("hello") == {'e': 1, 'o': 1}
    assert count_vowels("xyz") == {}

def test_is_substring():
    assert is_substring("hello", "ell") is True
    assert is_substring("cat", "dog") is False

if __name__ == "__main__":
    pytest.main()
