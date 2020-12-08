"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 8, 2020
Homework Problem 5.15.5
Description: This calculates the amount of money in savings given the principal, interest, and total years.
"""
def calc_compound_interest(principal, int_rate, years):
    """
    This calculates the compound interest non-recursively.
    :param principal: is the initial balance.
    :param int_rate: is the bank's interest rate.
    :param years: is the number of years to invest.
    :return: is the final bank balance.
    """
    return principal*((1+int_rate)**years)

def calc_compound_interest_recursive(principal, int_rate, years):
    """
    This calculates the compound interest recursively.
    :param principal: is the initial balance.
    :param int_rate: is the bank's interest rate.
    :param years: is the number of years to invest.
    :return: is the final bank balance.
    """
    if years == 0:
        return principal
    else:
        return (1+int_rate)*calc_compound_interest_recursive(principal,int_rate,years-1)

def main():
    while True:
        p = input("Please input your initial principal: ")
        rate = input("Please input your interest rate (Note that i is a decimal, not a percent interest rate: "
                     ".1 NOT 10%): ")
        years = input("Please input your years to invest: ")
        try:
            p = float(p)
            rate = float(rate)
            years = float(years)
            break
        except:
            print("Error: please enter valid numbers!")
    interest = round(calc_compound_interest(p, rate, years),4)
    recur_interest = round(calc_compound_interest_recursive(p, rate, years),4)
    equal = (interest == recur_interest)
    interest = round(interest, 2)
    recur_interest = round(recur_interest, 2)
    print("The non-recurisvely calculated final balance is", f'{interest:,}')
    print("The recurisvely calculated final balance is", f'{recur_interest:,}')
    if equal:
        print("The two values are equal (to four decimal places)!")
    else:
        print("The two values are NOT equal!")

if __name__ == "__main__":
    main()