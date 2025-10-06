
# Day 4 - Lists & Loops Exercises

# Exercise 1: Create a list of your 5 favorite foods and print each one using a loop
def favorite_foods_list():
    favorite_foods = ["Ramen", "Sushi", "Tacos", "Burgers", "Fried Chicken"]
    for foods in favorite_foods:
        print(foods)
    print("\n")

# Exercise 2: Ask the user for 3 numbers, store them in a list, and print the list sorted
def sort_numbers():
    numbers = []
    for _ in range(3):
        num = int(input("Please enter 3 numbers: "))
        numbers.append(num)
    numbers.sort()
    print("Sorted numbers:",numbers)

# Exercise 3: Write a function that takes a list of numbers and returns the sum
def sum_of_numbers(numbers):
    return sum(numbers)

# Exercise 4: Write a function that takes a list and returns the second largest number
def second_largest(numbers):
    numbers = list(set(numbers))    # Remove duplicates
    numbers.sort()
    if len(numbers) > 1:
        return numbers[-2]
    else:
        return "Not enough unique numbers"

# Exercise 5: Write a function that reverses a list without using [::-1] or reverse()
def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0,item) # Insert each item at the beginning
    return reversed_lst

if __name__ == "__main__":
    print("Exercise 1: Favorite Foods List")
    favorite_foods_list()

    print("\nExercise 2: Sorted Numbers")
    sort_numbers()

    numbers = [1,2,4,3,5]
    print("\nExercise 3: Sum of Numbers")
    print(sum_of_numbers(numbers))

    print("\nExercise 4: Second Largest")
    print(second_largest(numbers))

    print("\nExercise 5: Reverse List")
    print(reverse_list(numbers))


