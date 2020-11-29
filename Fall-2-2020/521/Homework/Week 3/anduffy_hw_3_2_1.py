"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: November 24, 2020
Homework Problem 2.1
Description: This is a program that counts the number of odds, evens, squares/cubes of an integer. This starts at 2 and
ends with 130.
"""

def odds_evens_squares_cubes(start, finish):
    """
    This is a program that counts the number of odds, evens, squares/cubes of an integer.
    :param start: is the first number checked in the sequence.
    :param finish: is the final number checked in the sequence.
    :return:
    """
    print("Checking numbers from ", start, " to ", finish)
    odds = 0
    odd_first_and_last = [0,0] #This and its even counterpart just store the first and last occurrences of even/odd nums
    evens = 0
    even_first_and_last = [0,0]
    squares = 0
    square_list = []
    top_square_found = False #This and the cubed counterpart check if the program has found the largest cubed value.
    cubes = 0
    cubes_list = []
    top_cube_found = False

    for val in range(start,finish+1):
        if val % 2 == 0: #Even
            evens += 1
            if even_first_and_last[0] == 0:
                even_first_and_last[0] = val
            else:
                even_first_and_last[1] = val
        else: #Odd
            odds += 1
            if odd_first_and_last[0] == 0:
                odd_first_and_last[0] = val
            else:
                odd_first_and_last[1] = val
        if top_square_found is False:
            if (val**2) < finish:
                squares += 1
                square_list.append(val**2)
            else:
                top_square_found = True
        if top_cube_found is False:
            if (val**3) < finish:
                cubes += 1
                cubes_list.append(val**3)
            else:
                top_cube_found = True

    print("Odd ("+ str(odds)+"): " + str(odd_first_and_last[0]) + "..." + str(odd_first_and_last[1]))
    print("Even ("+str(evens)+ "): " + str(even_first_and_last[0]) + "..." + str(even_first_and_last[1]))
    print("Square ("+ str(squares) + "): "+ str(square_list))
    print("Cube ("+str(cubes)+"): " + str(cubes_list))


def main():
    odds_evens_squares_cubes(2,130)

if __name__ == "__main__":
    main()