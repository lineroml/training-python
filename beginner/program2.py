# Write a program to iterate the first 10 numbers,
# and in each iteration, print the sum of the current
# and previous number.

def iterate_numbers(num):
    sum = 0
    print("Printing current and previous number sum in a range(10)")
    for i in range(num+1):
        if (i == 0):
            print("Current number 0 - Previous number 0 - SUM", sum)
        else:
            sum = 2*i - 1 #i+(i-1)
            print("Current number", i, "- Previous number", i-1, "SUM", sum)


num = int(input("Give me a number:"))
iterate_numbers(num)

