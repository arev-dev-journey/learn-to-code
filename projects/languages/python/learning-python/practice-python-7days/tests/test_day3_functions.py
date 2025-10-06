import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../exercises')))

from functions import add_numbers, even_or_odd, greet, factorial, find_largest

def test_add_numbers():
    assert add_numbers(5, 3) == "The sum of 5 and 3 is 8"

def test_even_or_odd():
    assert even_or_odd(4) == "4 is even"
    assert even_or_odd(5) == "5 is odd"

def test_greet():
    assert greet("Alex") == "Hello, Alex! Your favorite color is blue"
    assert greet("Alex", "green") == "Hello, Alex! Your favorite color is green"

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

def test_find_largest():
    assert find_largest([1, 9, 3, 2]) == 9
    assert find_largest([-5, -1, -10]) == -1

print("All tests passed!")
