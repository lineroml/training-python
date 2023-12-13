# Iterate the given list of numbers and print only those numbers which are divisible by 5

numbers = [10, 20, 33, 46, 55]


def print_divisible_by_five(array_of_numbers):
    divisible_by_five = []

    for num in numbers:
        if num%5 == 0:
            divisible_by_five.append(num)

    print("Given list is", numbers)
    print("Divisible by 5:", divisible_by_five)


print_divisible_by_five(numbers)