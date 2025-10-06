myList = [1,2,3,4,5,6,7,8,9,10]

for i in myList:
    print(i)

for num in myList:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd Number: {num}")
