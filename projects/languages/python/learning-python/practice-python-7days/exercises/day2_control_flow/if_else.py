# If/Else
age = 20
if age > 18:
    print("You are an adult")
else:
    print("You are a minor")

# Elif
temp = 75
if temp > 85:
    print("It's hot!")
elif temp > 65:
    print("It's nice outside")
else:
    print("It's cold")

'''
Comparison and Logical Operators
==
!=
>,<,>=.<=
and
or
nor
'''

# For loops
for i in range(5):
    print(i) # prints 0 to 4

# While loops
count = 0
while count < 5:
    print(count)
    count += 1

# Break/Continue
for i in range(10):
    if i == 5:
        break   # stops loop at 5
    print(i)

for i in range(5):
    if i == 2:
        continue    # skip when i == 2
    print(i)
