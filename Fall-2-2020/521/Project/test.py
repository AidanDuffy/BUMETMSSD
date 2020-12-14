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
    assert (card.checkBalance() == 300)
    assert (card.getCPP() == 1)
    assert (card.checkPointsOrCash() == "C")
    test = "template:Mastercard:Citi:Double Cash:C:SUB:False:Categories:" \
           "else-2:0:300"
    repstr = card.__repr__()
    assert (test == repstr)
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
    assert (sub.checkActive())
    assert (sub.getProgress() == 0)
    card.purchase(3000)
    assert (sub.getProgress() == 3000)
    card.purchase(1000)
    assert (sub.checkActive() is False)
    card.purchase(5000)
    assert (sub.getProgress() == 4000)
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
    assert (card1.checkWhichCategory("dining") == 2)
    assert (card2.checkWhichCategory("dining") == 8)
    assert (card2.checkWhichCategory("gas") == 2)
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