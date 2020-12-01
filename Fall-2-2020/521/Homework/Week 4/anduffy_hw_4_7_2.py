"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 1, 2020
Homework Problem 4.7.2
Description: Generates a new list, from some given list, that is the same length where
each element is the sum of its neighbor(s).
"""

def neighbor_sum_list(input_list):
    """
    This program generates a new list where each element is the sum of the original element
    plus the sum of its neighbor(s).
    :param input_list: is our original list
    :return:
    """
    list_length = len(input_list)
    new_list = []
    for i in range(0,list_length):
        sum = input_list[i]
        if (i != 0):
            sum += input_list[i-1]
        if (i != list_length - 1):
            sum += input_list[i+1]
        new_list.append(sum)
    print("Input List: ", input_list)
    print("Result List: ", new_list)

def main():
    input_list = [10,20,30,40,50]
    neighbor_sum_list(input_list)

if __name__ == "__main__":
    main()