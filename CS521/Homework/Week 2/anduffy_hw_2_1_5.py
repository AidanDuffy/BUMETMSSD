def main():
    """
    This method will ask the user for an integer, then, in 3 lines, it will determine whether that int is even or odd.
    :return:
    """
    number = input("Please input an integer: ")
    number = int(number)
    print(number%2)

if __name__ == "__main__":
    main()