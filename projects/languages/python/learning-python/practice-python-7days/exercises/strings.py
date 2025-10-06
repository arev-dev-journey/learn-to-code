# Day 5 - Strings & String Methods Exercises

# 1. Ask the user for a sentence and print it in all uppercase
def print_uppercase():
    user_input = input("Please enter a sentence: ")
    print(user_input.upper())

# 2. Count how many times a letter appears in a given string
def count_letter_occurrences(string, letter):
    count = 0
    for i in string:
        if i == letter:
            count += 1
    return count
# 3. Check if a word is a palindrome
def is_palindrome(word):
    reversed_word = word[::-1]
    if reversed_word.lower() == word.lower():
        return True
    else:
        return False

# 4. Count how many vowels are in a string
def count_vowels(string):
    counts = {}
    vowels = 'aeiou'

    for char in string.lower():
        if char in vowels:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

# 5. Return True if one string is a substring of the other
def is_substring(str1, str2):
    return str2.lower() in str1.lower()

if __name__ == "__main__":
    print("Exercise 1")
