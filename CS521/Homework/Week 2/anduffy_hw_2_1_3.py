def calculations(num):
    """
    This method will run and print the result of a number of calculations of additions and multiplications.
    :param num: is the integer that the calculations will be run on.
    :return:
    """
    result = num+num*num+num*num*num+num*num*num*num
    print(num, " + ",num, " * ", num, " + ", num, " * ", num," * ",num," + ",num," * ",num," * ",num," * ",num," = ", result)

def main():
    number = input("Please input an integer: ")
    number = int(number)
    calculations(number)

if __name__ == "__main__":
    main()