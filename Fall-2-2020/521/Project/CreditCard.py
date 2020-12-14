"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 15, 2020
Final Project
Description: This is a user-defined class, as requested in the project
guidelines that is for the creation of CreditCard objects.
"""


class CreditCard:

    def __init__(self, holder, network, issuer, name, sub_info, categories,
                 balance, age, points_cash_back, cpp = 1):
        """
        This constructs a new credit card with the given parameters. The main
        program will ensure everything is full passed in.
        :param holder: is the name of the card holder (private)
        :param network: is a string representing the card network (ie Visa)
        :param issuer: is a string representing the card issuer (ie Chase Bank)
        :param name: is a string of the actual name of the card, excluding the
        issuer name and the words credit card.
        :param sub_info: is a str representing the sign-up bonus information
        that will populate a custom SUB object.
        :param categories: is a dictionary with each category and the values
        are the percentage back in cash or point multiplier
        :param age: is the age of the card.
        :param points_cash_back: holds a char determining if this card is point
        or cash card
        :param cpp: is the cents per point (default to 1 for cash back)
        """
        self.__holder = holder
        self.network = network
        self.issuer = issuer
        self.card_name = name
        self.sub = SignUpBonus(sub_info)
        self.categories = self.buildCategories(categories)
        self.balance = int(balance)
        self.age = int(age)
        self.points_cash = points_cash_back
        self.cpp = float(cpp)
        if (self.age > self.sub.getMonths()):
            self.sub.deactivateSUB()

    def __repr__(self):
        """
        :return: this credit card in a format for the user cards text file
        """
        result = self.__getHolderName() + ":"
        result += self.network + ":" + self.issuer + ":" + self.card_name
        if self.checkPointsOrCash() == 'C':
            result += ":C:SUB:"
        else:
            result += ":P," + str(self.getCPP()) + ":SUB:"
        sub = self.sub
        result += str(sub.active)
        if sub.active:
            result += "," + sub.getReward() + "," + sub.getMin() + ","\
                      + sub.getProgress() + "," + sub.getMonths()
        result += ":Categories:"
        result += self.printCategories() + ":" + str(self.getAge()) + ":" \
                  + str(self.checkBalance())
        return result

    def purchase(self, cost):
        """
        This adds a purchase to the balance, and if the sign-up bonus is active
        then it will add it to the minimum spend progress as well.
        :param cost: is the value of the purchase
        :return: none.
        """
        self.balance += cost
        if self.sub.checkActive():
            self.sub.setProgress(cost)

    def __getHolderName(self):
        """
        :return: the name of the card holder. Private to protect the user's
        name.
        """
        return self.__holder

    def setHolderName(self, holder):
        """
        Sets the card holder's name
        :return: none
        """
        self.__holder = holder

    def checkBalance(self):
        """
        :return: the balance on this credit card.
        """
        return self.balance

    def getNetwork(self):
        """
        :return: the network associated with this card
        """
        return self.network

    def getIssuer(self):
        """
        :return: the issuer associated with this card
        """
        return self.issuer

    def getCardName(self):
        """
        :return: the name of this card
        """
        return self.card_name

    def payOffCard(self, debit):
        """
        This just lowers the balance after a user pays off their card.
        :param debit: is the amount they paid off.
        :return: none.
        """
        self.balance -= debit

    def getSUB(self):
        """
        :return: the sign-up bonus object associated with this card
        """
        return self.sub

    def checkPointsOrCash(self):
        """
        :return: the char P for points or C for cash back
        """
        return self.points_cash

    def getCPP(self):
        """
        :return: the float value for the cents per point for this card
        """
        return self.cpp

    def setCPP(self, cpp):
        """
        This sets a new cents per point value
        :param cpp: float, new cents per point value
        :return: none
        """
        self.cpp = cpp

    def getAge(self):
        """
        :return: the age, in months, of this card.
        """
        return self.age

    def getCategories(self):
        """
        :return: the dict of categories:cash back/points multiplier
        """
        return self.categories

    def buildCategories(self, cat):
        """
        This will take a string of categories and build a dictionary from it.
        :param cat: is the string of categories
        :return: the dictionary
        """
        category_list = list(cat.split(","))
        categories_dict = dict()
        for category in category_list:
            parts = list(category.split("-"))
            categories_dict[parts[0]] = float(parts[1])
        return categories_dict

    def checkWhichCategory(self, category):
        """
        This will take a given string category (i.e. dining) and check the
        rewards value.
        :param category: is the given string
        :return: an integer of percentage cash back or points multiplier
        """
        cat_dict = self.getCategories()
        if category in cat_dict.keys():
            return cat_dict.get(category)*self.getCPP()
        else:
            return cat_dict.get("else")*self.getCPP()

    def printCategories(self):
        """
        This takes the category dictionary and formats the content as a string
        to print.
        :return: the categories dictionary as a string for the save file.
        """
        cat_dict = self.getCategories()
        result = ""
        for category in cat_dict.keys():
            multiplier = (cat_dict.get(category))
            if multiplier.is_integer():
                multiplier = str(multiplier)
                result += category + "-" + multiplier[:len(multiplier)-1] + ","
            else:
                result += category + "-" + multiplier + ","
        return result[:len(result)-2] #Need to remove last comma

class SignUpBonus:
    """
    This is a custom object that is always tied to a specific card.
    """

    def __init__(self, info):
        """
        This creates a new sign-up bonus object given a string of info.
        :param info: is the SUB info provided by the database file or user.
        """
        if info == "False":
            self.active = False
            self.minimum = 0
            self.months = 0
            return
        sub = list(info.split(","))
        self.reward = int(sub[0])
        self.minimum = int(sub[1])
        self.months = int(sub[2])
        self.progress = 0
        if self.minimum == 0:
            self.active = False
        else:
            self.active = True

    def setProgress(self, progress):
        """
        This sets/updates the progress of a user's ability to get a sign-up
        bonus.
        :param progress: is the additional purchases in USD.
        :return: none
        """
        self.progress += progress
        if (self.progress >= self.minimum):
            self.deactivateSUB()

    def deactivateSUB(self):
        """
        This deactivates the sign-up bonus if the user hit the spend
        requirement or ran out of time.
        :return:
        """
        self.active = False

    def checkActive(self):
        """
        This just checks if the SUB is active or not.
        :return: True or False, depending on the the activity of the SUB
        """
        return self.active

    def getMonths(self):
        """
        This gives the user the number of months left on the SUB.
        :return:
        """
        return self.months

    def getReward(self):
        """
        :return: the reward for this sign up bonus.
        """
        return self.reward

    def getProgress(self):
        """
        :return: the progress towards the minimum spend for this SUB
        """
        return self.progress

    def getMin(self):
        """
        :return: the minimum spending requirement for this SUB.
        """
        return self.minimum