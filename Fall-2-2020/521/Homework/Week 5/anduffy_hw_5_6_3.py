"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 8, 2020
Homework Problem 5.6.3
Description: This takes in three numbers and performs some quick calculations.
"""

def main():
    nums = input("Please input 3 numbers separated by commas (ie 1,2,3): ")
    num_array = []
    try:
        num_str_array = nums.split(",")
        for i in range(0,3):
            num_array.append(float(num_str_array[i]))
        if num_array[1] == 0:
            print("You are attempting to divide by zero!")
            raise Exception(ZeroDivisionError)
    except:
        print("Please try again with 3 numbers, separated by commas!")
        raise Exception(ValueError)
    answer = (num_array[0]/num_array[1]) + num_array[2]
    print(num_array[0], "/", num_array[1], "+", num_array[2], "=", '{:.2f}'.format(answer))

if __name__ == "__main__":
    main()