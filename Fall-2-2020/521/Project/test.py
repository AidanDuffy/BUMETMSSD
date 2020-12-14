"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 15, 2020
Final Project
Description: This is a test file that is meant to check functions are working
properly
"""

import CreditCard

def testSetupAndChanges():
    holder = "template"
    network = "Mastercard"
    issuer = "Citi"
    name = "Double Cash"
    sub_info = "0,0,0"
    categories = "else-2"
    balance = 0
    age = 0
    points_cash_back = "C"
    card = CreditCard.CreditCard(holder, network, issuer, name, sub_info,
                                 categories, balance, age,points_cash_back)
    card.purchase(1000)
    card.payOffCard(700)
    if card.checkBalance() != 300:
        return False
    if card.getCPP() != 1:
        return False
    if card.checkPointsOrCash() != "C":
        return False
    test = "template:Mastercard:Citi:Double Cash:C:SUB:False:Categories:" \
           "else-2:0:300"
    repstr = card.__repr__()
    if repstr != test:
        return False
    return True

def testSUB():
    holder = "template"
    network = "AMEX"
    issuer = "AMEX"
    name = "Gold"
    sub_info = "60000,4000,6"
    categories = "dining-4,grocery-4,flight(AMEX)-3,else-1"
    balance = 0
    age = 0
    points_cash_back = "P"
    cpp = 2
    card = CreditCard.CreditCard(holder, network, issuer, name, sub_info,
                                 categories,balance, age,points_cash_back, cpp)
    sub = card.getSUB()
    if sub.checkActive() is False:
        return False
    if sub.getProgress() != 0:
        return False
    card.purchase(3000)
    if sub.getProgress() != 3000:
        return False
    card.purchase(1000)
    if sub.checkActive() is True:
        return False
    card.purchase(5000)
    if sub.getProgress() != 4000:
        return False
    return True

def testSelectCategory():
    holder = "template"
    network = "Mastercard"
    issuer = "Citi"
    name = "Double Cash"
    sub_info = "0,0,0"
    categories = "else-2"
    balance = 0
    age = 0
    points_cash_back = "C"
    card1 = CreditCard.CreditCard(holder, network, issuer, name, sub_info,
                                  categories, balance, age, points_cash_back)
    holder = "template"
    network = "AMEX"
    issuer = "AMEX"
    name = "Gold"
    sub_info = "60000,4000,6"
    categories = "dining-4,grocery-4,flight(AMEX)-3,else-1"
    balance = 0
    age = 0
    points_cash_back = "P"
    cpp = 2
    card2 = CreditCard.CreditCard(holder, network, issuer, name, sub_info,
                                  categories, balance, age, points_cash_back,
                                  cpp)
    if card1.checkWhichCategory("dining") != 2:
        return False
    if card2.checkWhichCategory("dining") != 8:
        return False
    if card2.checkWhichCategory("gas") != 2:
        return False
    return True

def main():
    check = testSetupAndChanges()
    if check:
        print("Initial setup and basic change test passed!")
    else:
        print("Initial setup and basic change test failed...")
    check = testSUB()
    if check:
        print("Sign-up bonus test passed!")
    else:
        print("Sign-up bonus test failed...")
    check = testSelectCategory()
    if check:
        print("Category Selection test passed!")
    else:
        print("Category Selection test failed...")

if __name__ == "__main__":
    main()