# Write a function to return True if the first and last
# number of a given list is same. If numbers are different
# then return False.

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def first_and_last(array_of_nums):
    if (array_of_nums[0] == array_of_nums[-1]):
        return True
    else:
        return False

print(first_and_last(numbers_x))
print(first_and_last(numbers_y))

