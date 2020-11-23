def bmi(weight, height, measure):
    """
    This method calculates and prints a user's BMI, or body mass index.
    :param weight: is the user's weight.
    :param height: is the user's height.
    :param measure: is K for metric, I for imperial.
    :return:
    """
    if measure == "I":
        weight = weight * 0.45359237
        height = height / 39.270
    print(weight / (height ** 2))


def main():
    kilo_or_pounds = input("Please input M if you plan on using the metric system, I for the imperial system: ")
    if kilo_or_pounds != "K" and kilo_or_pounds != "I":
        print("Please run again and enter a valid character!")
        exit()
    weight = input("Please input your weight in kgs or lbs: ")
    height = input("Please input your height in meters or inches: ")
    bmi(float(weight), float(height), kilo_or_pounds)


if __name__ == "__main__":
    main()
