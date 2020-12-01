"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 1, 2020
Homework Problem 4.9.3
Description: This creates a dictionary of first (V) and last (K) names.
"""

def name_dictionary(first_names,last_names):
    """
    Takes in lists of first and last names, then creates a dictionary from that.
    :param first_names: This is the list of all the first names
    :param last_names: This is the list of all the last names
    :return:
    """
    name_dict = dict(zip(last_names,first_names))
    print("First Names: ", first_names)
    print("Last Names: ", last_names)
    print("Name Dictionary: ", name_dict)

def main():
    first_names = ['Jane','John','Jack','Will']
    last_names = ['Doe','Deere','Black','Ferrell']
    name_dictionary(first_names,last_names)

if __name__ == "__main__":
    main()