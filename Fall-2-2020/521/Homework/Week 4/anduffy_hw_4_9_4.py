"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 1, 2020
Homework Problem 4.9.4
Description: This prints keys, values, key-value pairs, pairs in order of key as well as
in order of value.
"""

def print_dict(my_dict):
    """
    This prints keys, values, key-value pairs, pairs in order of key as well as
    in order of value.
    :param my_dict: is the input dictionary.
    :return:
    """
    keys = str(my_dict.keys())
    vals = str(my_dict.values())
    key_val_pairs = str(my_dict.items())
    key_val_pairs_sorted_keys = str(sorted(my_dict.items()))
    key_val_pairs_sorted_vals = ""
    for val in sorted(my_dict, key = my_dict.get):
        key_val_pairs_sorted_vals += (str(val) + ": " + str(my_dict[val])) + ", "
    #The reformatting below just makes the print statements more readable
    print("a. Keys: ", keys[10:len(keys)-1])
    print("b. Values: ", vals[13:len(vals)-2])
    print("c. Key value pairs: ", key_val_pairs[11:len(key_val_pairs)-1])
    print("d. Key value pairs ordered by key: ", key_val_pairs_sorted_keys)
    print("e. Key value pairs ordered by val: ", key_val_pairs_sorted_vals[:len(key_val_pairs_sorted_vals)-2])

def main():
    my_dict = {'a':15,'c':18,'b':20}
    print_dict(my_dict)

if __name__ == "__main__":
    main()