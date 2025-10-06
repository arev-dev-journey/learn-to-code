def calc_avg(numbers):
    sum = 0
    avg = 0
    for num in numbers:
        sum += num
        avg = sum / len(numbers)

    return avg


numbers = [1,2,3,4,5]

print(calc_avg(numbers))


def calc_avg_w_func(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0

print(calc_avg_w_func(numbers))
