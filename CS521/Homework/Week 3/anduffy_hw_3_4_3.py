"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: November 24, 2020
Homework Problem 4.3
Description: This a program that will prompt a user for a sentence then will calculate the number of
uppercase, lowercase, digits, and punctuation symbols.
"""

def sentence_analysis(sentence):
    """
    This calculates the number of uppercase letters, lowercase, digits, and punctuation symbols.
    :param sentence: is the given sentence.
    :return:
    """
    punctuation = "!.?;:,"
    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = "abcdefghijklmnopqrstuvqxyz"
    uppers = 0
    lowers = 0
    digits = 0
    puncts = 0

    for char in sentence:
        if char in punctuation:
            puncts += 1
        elif char in upper_alpha:
            uppers += 1
        elif char in lower_alpha:
            lowers += 1
        else:
            try:
                int(char)
                digits += 1
            except: #This is if it fails to fit into any of the categories.
                continue
    print("# Upper   # Lower   # Digits  # Punct.")
    print("--------  --------  --------  --------")
    print("   " + str(uppers) + "         " + str(lowers) + "        ", str(digits), "       ", str(puncts))

def main():
    sentence = input("Please input a sentence for analysis: ")
    sentence_analysis(sentence)

if __name__ == "__main__":
    main()