def print_string_int_fp(inp):
    """
    This takes a given input and prints out the input as a string, integer, and a floating point.
    :param inp: is the user-defined input that will be outputted in several formats
    :return:
    """
    str_val = str(inp)
    int_val = int(inp)
    fp_val = float(inp)
    print("String: ", str_val, " Integer: ", int_val, " Float: ", fp_val)
    """
    This method can take integers without throwing any errors. Characters, floats, and strings, will all
    run into errors with the int() method.
    """


def main():
    user_input = input("Please provide an input to be output as a string, int, and float:  ")
    print_string_int_fp(user_input)


if __name__ == "__main__":
    main()
