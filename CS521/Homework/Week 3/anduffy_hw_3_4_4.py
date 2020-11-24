"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: November 24, 2020
Homework Problem 4.4
Description: This intakes a 3 digit number s.t. all digits are ascending and checks all these parameters are met.
"""

def three_ascending_digits():
    """
    This loops and asks for a user to input a 3 digit number with ascending digits. It will continue until these
    conditions are met.
    :return:
    """
    while True:
        three_digits = input("Please enter a 3-digit integer with ascending digits: ")
        try:
            int_digits = int(three_digits)
            if len(three_digits) != 3:
                print("Error: You did not enter a 3-digit number.")
                continue
            digit_list = [int(three_digits[0]),int(three_digits[1]),int(three_digits[2])]
            if digit_list[0] == digit_list[1] or digit_list[0] == digit_list[2] or digit_list[1] == digit_list[2]:
                print("Your number contains a duplication! Try again")
            elif digit_list[0] > digit_list[1] or digit_list[1] > digit_list[2]:
                print("Error: The digits are not in ascending order! Try again.")
            else:
                print("Number accepted!")
                break
        except:
            print("Error: This is not an integer! Please try again.")
            continue

if __name__ == '__main__':
    three_ascending_digits()