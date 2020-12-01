"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 1, 2020
Homework Problem 4.9.6
Description: Gets a number from a user, converts the number to words using a dictionary and prints that.
"""

def number_as_word(number):
    """
    Gets a number from a user, converts the number to words using a dictionary and prints that.
    :param number: is the input provided by the user.
    :return:
    """
    num_dict = {".":"Point", "0":"Zero", "1":'One', "2":'Two',
                "3":"Three","4":"Four","5":"Five","6":"Six",
                "7":"Seven","8":"Eight","9":"Nine", "-":"Negative"}
    output = "As Text:"
    for digit in number:
        output += " " + num_dict[digit]
    print(output)

def main():
    given_number = False
    while given_number is False:
        try:
            number = (input("Enter a number: "))
            if ',' in number:
                print("Please try again without entering commas.")
            else:
                number_as_int = float(number)
                given_number = True
                number_as_word(number)
        except:
            print("Please enter a valid number! \"", number, "\" is not a valid number.", sep='')

if __name__ == "__main__":
    main()