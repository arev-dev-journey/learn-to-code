def say_hello():
    print('Hello')
def say_hello(name):
    print(f'Hello {name}')

say_hello('Alex')

def say_hello(name='Default'):
    print(f'Hello {name}')

say_hello()

def add_num(num1, num2):
    return num1+num2

result = add_num(10,20)
print(result)

def print_result(a,b):
    print(a+b)

def return_result(a,b):
    return a + b

result = print_result(10,20)

result = return_result(10,3)
print(result)

def myfunc(a,b):
    print(a+b)
    return a + b

result = myfunc(10,20)

def sum_nums(num1,num2):
    return num1 + num2

sum_nums(10,20)

print(sum_nums(10,23))
