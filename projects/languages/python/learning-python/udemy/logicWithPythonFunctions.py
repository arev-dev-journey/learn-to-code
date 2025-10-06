def even_check(number):
    return number % 2 == 0

#Return true if any number is even inside a list
def check_even_list(num_list):

    for number in num_list:
        if number % 2 == 0:
            return True 
        else:
           pass 

print(check_even_list([1,3,5]))

