"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 8, 2020
Homework Problem 5.8.4
Description: This will receive a file name, read and convert the words to a list. It will generate a list
of words that appear only once.
"""

def list_to_words(word_list):
    """
    This returns all words in the file word list that appear once.
    :param word_list: is the original list of words
    :return: is the word list of words that appear only once.
    """
    singles = []
    removed = []
    for word in word_list:
        cur = word.upper()
        if cur[len(cur) - 1] == ".":
            cur = cur[:len(cur) - 2]
        if cur in singles:
            removed.append(cur)
            singles.remove(cur)
        else:
            singles.append(cur)
    return singles

def main():
    file = input("Please input the text file name: ") + ".txt"
    file = open(file, "r")
    word_list = []
    for line in file:
        for word in line.split():
            word_list.append(word)
    single_word_list = list_to_words(word_list)
    print("The following is a list of words that appear only once in the given file:", single_word_list)
    file.close()

if __name__ == "__main__":
    main()