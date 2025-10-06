''' 
1. Create two variables: x = 8 and y = 3, and print the sum, difference, product, and quotient
2. Ask the user for their name and favorite color, then print a sentence that says:
"Hi [name]! Your favorite color is [color]"
3. Ask the user for two numbers and print their product
4. Write a program that calculates the remainder when dividing one number by another
'''
# Exercise 1: Sum, difference, product, quotient
x = 8
y = 3
print("Exercise 1: Sum, difference, product, quotient")
print(f"Sum: {x + y}")
print(f"Difference: {x - y}")
print(f"Product: {x * y}")
print(f"Quotient: {x / y}\n")

# Exercise 2: Name and color
print("Exercise 2: Name and Color")
name = input("Please enter your name: \n")
color = input("Please enter your favorite color: \n")
print(f'Hi {name}! Your favorite color is {color}\n')

# Exercise 3: Product of two numbers
print("Exercise 3: Product of two numbers")
user_input = input("Enter two numbers, separated by a space: ")
num1, num2 = user_input.split()

num1 = int(num1)
num2 = int(num2)

product = num1 * num2

print(f"The product of {num1} and {num2} is {product}\n")

# Exercise 4: Remainder
print("Exercise 4: Remainder")
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))
result = num1 % num2
print(f"The remainder of {num1} and {num2} is {result}")
