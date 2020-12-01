"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 1, 2020
Homework Problem 4.9.5
Description: This program creates a dictionary with letter frequency, a string of the most common letter(s)
and a histogram of letter frequencies.
"""

def sentence_word_freq(sentence):
    """
    This program creates a dictionary with letter frequency, a string of the most common letter(s)
    and a histogram of letter frequencies.
    :param sentence: is the input sentence.
    :return:
    """
    print("The string being analyzed is: ", sentence)
    sentence_dict = dict()
    max_frequency = 0
    max_frequency_list = []
    for char in sentence:
        if char == ' ':
            continue
        if char in sentence_dict:
            sentence_dict[char] += 1
            if sentence_dict[char] > max_frequency:
                max_frequency = sentence_dict[char]
                max_frequency_list = list()
                max_frequency_list.append(char)
            elif sentence_dict[char] == max_frequency:
                max_frequency_list.append(char)
        else:
            sentence_dict[char] = 1
    print("1. Sorted dictionary of letter counts: ", sorted(sentence_dict.items()))
    if len(max_frequency_list) == 1:
        print("2. Most frequent letter \"", max_frequency_list[0], "\" appears ", max_frequency, " times.", sep='')
    else:
        print("2. Most frequent letters", max_frequency_list, "appears", max_frequency, "times.")
    print("3. Histogram:")
    for key in sorted(sentence_dict.keys()):
        print(key*sentence_dict[key])

def main():
    sentence = str(input("Please input a sentence that is at least 15 characters long: ")).upper()
    if len(sentence) < 15:
        raise Exception("Please enter a sentence with more than 15 characters!")
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in sentence:
        if char not in alpha and char != ' ':
            raise Exception("Please only input letters! Try again")
    sentence_word_freq(sentence)

if __name__ == "__main__":
    main()