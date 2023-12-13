# Write a program to accept a string from the user
# and display characters that are present at an even
# index number.

def even_characters(str):
    for i in range(len(str)):
        if i % 2 == 0:
            print(str[i])


str = input("Please give me a string ty :) :")
print(str[0::2])
