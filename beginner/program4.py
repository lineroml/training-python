# Write a program to remove characters from a string
# starting from zero up to n and return a new string.
#
# For example:
#
# remove_chars("pynative", 4) so output must be tive.
# Here, we need to remove the first four characters from a string.
# remove_chars("pynative", 2) so output must be native.
# Here, we need to remove the first two characters from a string.
# Note: n must be less than the length of the string.

def remove_chars(stringg, numero):
    if numero > len(stringg):
        return "Bitch wot."
    else:
        return stringg[numero-len(stringg):len(stringg)]


strs = input("Dame una string:")
nums = int(input("Dame un numero:"))

print(remove_chars(strs, nums))