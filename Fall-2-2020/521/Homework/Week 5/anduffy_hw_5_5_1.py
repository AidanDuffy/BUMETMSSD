"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 8, 2020
Homework Problem 5.5.1
Description: This takes a sentence, counts # of vowels and consonants, and returns a dict of those counts and prints
them.
"""

def vc_counter(sentence):
    """
    This counts the vowels and consonants of a given string.
    :param sentence: is the user input string.
    :return: this is the dictionary of the vowel/consonant counts.
    """
    vowels_and_consonants = dict()
    vowels_and_consonants["vowels"] = 0
    vowels_and_consonants["consonants"] = 0
    vowels = "AEIOU"
    cons = "BCDFGHJKLMNPQRSTVWXYZ"
    sentence = sentence.upper()
    for char in sentence:
        if char in vowels:
            vowels_and_consonants["vowels"] += 1
        elif char in cons:
            vowels_and_consonants["consonants"] += 1
        else:
            continue
    return vowels_and_consonants


def main():
    sentence = input("Please input an English sentence: ")
    dict = vc_counter(sentence)
    print("There are" , str(dict["vowels"]), "vowels and", str(dict["consonants"]), "consonants in the given sentence.")


if __name__ == "__main__":
    main()