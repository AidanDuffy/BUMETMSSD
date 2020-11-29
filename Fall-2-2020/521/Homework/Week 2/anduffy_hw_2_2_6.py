def leap_years():
    """
    This calculates and prints all of the leap years between 1900 & 2020 twice: once with a for loop and once with a
    while loop.
    :return:
    """
    print("For Loop: ")
    for i in range(1900, 2021):
        if i % 4 == 0:
            if i % 100 == 0:
                if i % 400 == 0:
                    print(i)
                else:
                    continue
            else:
                print(i)
    print("===========================")  # This is just to make the result more readable
    print("While Loop: ")
    year = 1900
    while year <= 2020:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(year)
                else:
                    year += 1
                    continue
            else:
                print(year)
        year += 1


def main():
    leap_years()


if __name__ == "__main__":
    main()
