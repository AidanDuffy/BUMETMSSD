def factors(x):
    """
    This prints out all of the factors of a user-defined integer.
    :param x: is the integer the user provided.
    :return:
    """
    i = 1
    while i <= x:
        if x % i == 0:
            print(i)
        i += 1


def main():
    """
    This is just a given for loop being rewritten as a while loop.
    :return:
    """
    x = input("Please input an integer: ")
    x = int(x)
    factors(x)


if __name__ == "__main__":
    main()
