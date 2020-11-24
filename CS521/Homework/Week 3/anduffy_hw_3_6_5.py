"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: November 24, 2020
Homework Problem 6.5
Description: Reads a file of 20 words, inserts new line characters and writes a new text file thats 4 lines of 5 words.
"""
def restructure_file():
    try:
        original = open("originl.txt", "r")
    except:
        print("Error: The input file does not exist!")
        return
    new_file = open("new.txt", "w")
    file_contents = original.read()
    file_words = file_contents.split()
    if len(file_words) != 20:
        print("Error: The given file is not 20 words.")
    else:
        count = 0 #This keeps track of every fifth word.
        for word in file_words:
            if count % 5 == 0 and count != 0:
                new_file.write("\n")
            new_file.write(word + " ")
            count += 1
    original.close()
    new_file.close()

if __name__ == "__main__":
    restructure_file()