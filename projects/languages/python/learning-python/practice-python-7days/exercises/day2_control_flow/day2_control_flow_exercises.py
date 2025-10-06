'''
Day 2 Control Flow Exercises
1. Ask the user for a number and tell them if it's even or odd
2. Ask the user for a grade(0-100) and print letter value
3. Print numbers 1 to 10 using a for loop
4. Print numbers 10 to 1 using a while loop
5. Ask the user to enter numbers continuosly (in a while loop) and stop when they enter 0.
Then print the sum of all entered numbers
'''
# Exercise 1: Even or Odd
print("Exercise 1: Even or Odd")
user_input = int(input("Enter a number to determine if it's even or odd\n"))
if user_input % 2 == 0:
    print(f"{user_input} is even\n")
else:
    print(f"{user_input} is odd\n")

# Exercise 2: Grade Checker
print("Exercise 2: Grade Checker")
grade = int(input("Enter a number grade to determine letter grade\n"))
if grade >= 90 and grade <= 100:
    print('A\n')
elif grade >= 80 and grade < 90:
    print('B\n')
elif grade >= 70 and grade < 80:
    print('C\n')
elif grade >= 60 and grade < 70:
    print('D\n')
else:
    print('F\n')

# Exercise 3: Print numbers 1-10 with for loop
print("Exercise 3: Print Numbers 1-10 with for loop")
for i in range(1, 11):
    print(i)
print('\n')

# Exercise 4: Print numbers 10-1 with while loop
print("Exercise 4: Print numbers 10-1 with while loop")
count = 10
while count > 0:
    print(count)
    count -= 1
print('\n')

# Exercise 5: Continuos number input sum until 0
print("Exercise 5: Continous number input sum until 0")
total = 0
while True:
    user_num = int(input("Enter a number (0 to stop): "))
    if user_num == 0:
        break
    total += user_num
print(f"The total of all numbers entered is: {total}")


