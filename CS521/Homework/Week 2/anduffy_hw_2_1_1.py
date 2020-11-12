def calculation_check(number):
    """
    This method takes in the given number from the user, runs a series of calculations, then checks if the resulting
    number is the same as the input. It prints out which is the case.
    :param number: is the input given by the user in main()
    """
    calculated_number = (((number+2)*3)-6)/3
    if calculated_number == number:
        print("After running a series of calculations, the resulting number was the"
              " same as the one the user input.")
    else:
        print("After running a series of calculations, the resulting number was "
              "different from the one the user input.")


def main():
    number = input("Please input a number: ")
    number = float(number)
    calculation_check(number)

if __name__ == "__main__":
    main()