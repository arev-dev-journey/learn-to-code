import sys
import os
import pytest

# Add the exercises/day4 directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../exercises')))

from lists import sum_of_numbers, second_largest, reverse_list, sort_numbers, favorite_foods_list

from unittest.mock import patch

def test_sum_of_numbers():
    assert sum_of_numbers([1, 2, 3, 4, 5]) == 15
    assert sum_of_numbers([-1, 1]) == 0

def test_second_largest():
    assert second_largest([1, 2, 3, 4, 5]) == 4
    assert second_largest([10, 10, 5, 7]) == 7
    assert second_largest([1]) == "Not enough unique numbers"

def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([]) == []
    assert reverse_list([5]) == [5]

def test_sort_numbers(capsys):
    # Pretend the user enters 9, 3, and 7 when asked for numbers
    inputs = ['9', '3', '7']
    with patch('builtins.input', side_effect=inputs):
        sort_numbers()
    # Capture printed output
    captured = capsys.readouterr()
    assert "Sorted numbers: [3, 7, 9]" in captured.out

def test_favorite_foods_list(capsys):
    favorite_foods_list()
    captured = capsys.readouterr()
    assert "Ramen" in captured.out
    assert "Sushi" in captured.out
    assert "Fried Chicken" in captured.out


# Note: tests for functions that take input (like sort_numbers or favorite_foods_list)
# are harder to test with automated input and usually require mocking input().
# We can skip those for now or refactor later.

if __name__ == "__main__":
    pytest.main()

