# Day 7 - Classes & Objects Exercises

# Exercise 1: Define a class `Car` with attributes make, model, and year
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Exercise 2: Add a method `describe` to print car details
    def describe(self):
        return f"{self.make} {self.model} {self.year}"

# Exercise 3: Create a method `is_classic()` that returns True if year < 2000
    def is_classic(self):
        return self.year < 2000

# Exercise 4: Define a `Person` class with name and age attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Exercise 5: Add a method `birthday()` that increases age by 1
    def birthday(self):
        self.age += 1
        return f"Happy Birthday, {self.name}! You are now {self.age} years old!"

if __name__ == "__main__":
    myCar = Car("BMW", "X3", 2021)
    myCar.describe()
    print(myCar.is_classic())
    person1 = Person("Alex",31)
    print(person1.birthday())
    print(person1.birthday())
