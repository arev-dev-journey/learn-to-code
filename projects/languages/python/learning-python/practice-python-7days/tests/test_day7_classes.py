import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../exercises')))

from classes import Car, Person

def test_car_initialization():
    car = Car("BMW","X3",2021)
    assert car.make == "BMW"
    assert car.model == "X3"
    assert car.year == 2021

def test_describe():
    my_car = Car("BMW","X3",2021)
    assert my_car.describe() == "BMW X3 2021"
    
def test_is_classic():
    car = Car("BMW","X3",2021)
    assert car.is_classic() is False

def test_person_initialization():
    person = Person("Alex",32)
    assert person.name == "Alex"
    assert person.age == 32

def test_birthday():
    person = Person("Alex",31)
    person.birthday()
    assert person.age == 32
    person.birthday()
    assert person.age == 33
