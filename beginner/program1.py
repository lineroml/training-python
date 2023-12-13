# Given two integer numbers, return their product only
# if the product is equal to or lower than 1000.
# Otherwise, return their sum.


def bitch_function(num1,num2):
    prod = num1 * num2
    if prod <= 1000:
        return prod
    else:
        return num1+num2


#main xd
number1 = int(input("Enter num1: "))
number2 = int(input("Enter num2: "))

print("The result is", bitch_function(number1, number2))