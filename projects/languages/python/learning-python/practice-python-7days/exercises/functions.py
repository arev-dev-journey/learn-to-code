
'''
Day 3 - Functions Exercises
1. Write a function that takes two numbers and returns their sum
2. Write a function that checks if a number is even or odd, and returns a string
3. Write a function that takes a name and a favorite color (default "blue") and prints a message
4. Write a function that returns the factorial of a given number
5. Write a function that takes a list of numbers and returns the largest number
'''

# Exercise 1
def add_numbers(a, b):
    return f"The sum of {a} and {b} is {a+b}"

# Exercise 2
def even_or_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

# Exercise 3
def greet(name, color="blue"):
    return f"Hello, {name}! Your favorite color is {color}"

# Exercise 4
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Exercise 5
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Optional: Example calls here if you want to test
if __name__ == "__main__":
    # Example: print(add_numbers(3,4))
    print(add_numbers(3,4))
    print(even_or_odd(3))
    print(greet("Alex","red"))
    print(greet("Alex"))
    print(factorial(5))
    print(find_largest([3,9,2,15,6]))
