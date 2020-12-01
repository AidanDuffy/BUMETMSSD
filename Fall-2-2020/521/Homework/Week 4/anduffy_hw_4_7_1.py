"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 1, 2020
Homework Problem 4.7.1
Description: Uses list comprehension to find the sums of all even and odd integers in a given list.
"""

def odds_and_evens_sums(sum_list):
    """
    Prints out the sum of all the evens then all of the odds of a list of integers
    from 1 to 10 inclusive using list comprehension.
    :param sum_list: The list of ints from 1 to 10 inclusive
    :return:
    """
    odd_sum = 0
    even_sum = 0
    for num in sum_list:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    print("Evaluating the numbers in: ", sum_list)
    print("Even: ", even_sum)
    print("Odd: ", odd_sum)


def main():
    sum_list = [1,2,3,4,5,6,7,8,9,10]
    odds_and_evens_sums(sum_list)

if __name__ == "__main__":
    main()