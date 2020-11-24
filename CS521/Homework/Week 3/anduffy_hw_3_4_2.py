"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: November 24, 2020
Homework Problem 4.2
Description: Checks if a constant string has an even or odd length
"""

CONSTANT_STRING = "My name is Aidan Duffy."

def check_constant_str_length(const_string):
    """
    This checks whether the length of the given string is even or odd.
    :param const_string: is the given constant string.
    :return:
    """
    string_len = len(const_string)
    if string_len % 2 == 0:
        print("This string is even! Try again with an odd string.")
    else:
        print("My " + str(string_len) + " character string is: \"" + const_string + "\"")
        print("The middle character is: \"" + const_string[string_len//2] + "\"")
        print("The 1st half of the string is: \"" + const_string[:string_len//2] + "\"")
        print("The 2nd half of the string is: \"" + const_string[string_len//2 + 1:] + "\"")

def main():
    check_constant_str_length(CONSTANT_STRING)

if __name__ == "__main__":
    main()