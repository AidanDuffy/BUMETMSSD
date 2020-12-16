"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 15, 2020
Final Project
Description: This is a user-defined class, as requested in the project
guidelines that is for the creation of CreditCard objects.
Future Goals: Consolidate constructor, allow for other constructors.
Allow for subcategories built in from the parse file.
"""


class CreditCard:

    def __init__(self, holder, network, issuer, name, sub_info, categories,
                 balance, age, points_cash_back, cpp=1):
        """
        This constructs a new credit card with the given parameters. The main
        program will ensure everything is full passed in.
        :param holder: is the name of the card holder (private)
        :param network: is a string representing the card network (ie Visa)
        :param issuer: is a string representing the card issuer (ie Chase Bank)
        :param name: is a string of the actual name of the card, excluding the
        issuer name and the words credit card.
        :param sub_info: is a str representing the sign-up bonus information
        that will populate a custom sign_up_bonus object.
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
        self.categories = self.build_categories(categories)
        self.balance = int(balance)
        self.age = int(age)
        self.points_cash = points_cash_back
        self.cpp = float(cpp)
        if (self.points_cash == "P"):
            self.sub.set_return_on_spend(self.get_cents_per_point())
        if (self.age > self.sub.get_months()):
            self.sub.deactivate_sign_up_bonus()

    def __repr__(self):
        """
        :return: this credit card in a format for the user cards text file
        """
        result = self.__get_holder_name() + ":"
        result += self.network + ":" + self.issuer + ":" + self.card_name
        if self.check_points_or_cash() == 'C':
            result += ":C:SUB:"
        else:
            result += ":P," + str(self.get_cents_per_point()) + ":SUB:"
        sub = self.sub
        result += str(sub.active)
        if sub.active:
            result += "," + str(sub.get_reward())+ "," +\
                      str(sub.get_minimum_spend())+"," \
                      + str(sub.get_progress()) + "," + str(sub.get_months())
        result += ":Categories:"
        result += self.print_categories() + ":" + str(self.get_age()) + ":" \
                  + str(self.check_balance())
        return result

    def purchase(self, cost):
        """
        This adds a purchase to the balance, and if the sign-up bonus is active
        then it will add it to the minimum spend progress as well.
        :param cost: is the value of the purchase
        :return: none.
        """
        self.balance += cost
        if self.sub.check_active():
            self.sub.set_progress(cost)

    def __get_holder_name(self):
        """
        :return: the name of the card holder. Private to protect the user's
        name.
        """
        return self.__holder

    def set_holder_name(self, holder):
        """
        Sets the card holder's name
        :return: none
        """
        self.__holder = holder

    def check_balance(self):
        """
        :return: the balance on this credit card.
        """
        return self.balance

    def get_network(self):
        """
        :return: the network associated with this card
        """
        return self.network

    def get_issuer(self):
        """
        :return: the issuer associated with this card
        """
        return self.issuer

    def get_card_name(self):
        """
        :return: the name of this card
        """
        return self.card_name

    def pay_off_card(self, debit):
        """
        This just lowers the balance after a user pays off their card.
        :param debit: is the amount they paid off.
        :return: none.
        """
        self.balance -= debit

    def get_sign_up_bonus(self):
        """
        :return: the sign-up bonus object associated with this card
        """
        return self.sub

    def check_points_or_cash(self):
        """
        :return: the char P for points or C for cash back
        """
        return self.points_cash

    def get_cents_per_point(self):
        """
        :return: the float value for the cents per point for this card
        """
        return self.cpp

    def set_cents_per_point(self, cpp):
        """
        This sets a new cents per point value
        :param cpp: float, new cents per point value
        :return: none
        """
        self.cpp = cpp

    def get_age(self):
        """
        :return: the age, in months, of this card.
        """
        return self.age

    def get_categories(self):
        """
        :return: the dict of categories:cash back/points multiplier
        """
        return self.categories

    def build_categories(self, cat):
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

    def check_categories(self, category):
        """
        This will take a given string category (i.e. dining) and check the
        rewards value.
        :param category: is the given string
        :return: an integer of percentage cash back or points multiplier
        """
        cat_dict = self.get_categories()
        if category in cat_dict.keys():
            return cat_dict.get(category) * self.get_cents_per_point()
        else:
            return cat_dict.get("else") * self.get_cents_per_point()

    def print_categories(self):
        """
        This takes the category dictionary and formats the content as a string
        to print.
        :return: the categories dictionary as a string for the save file.
        """
        cat_dict = self.get_categories()
        result = ""
        for category in cat_dict.keys():
            multiplier = (cat_dict.get(category))
            if multiplier.is_integer():
                multiplier = str(multiplier)
                result += category + "-" + multiplier[
                                           :len(multiplier) - 1] + ","
            else:
                result += category + "-" + str(multiplier) + ","
        return result[:len(result) - 2]  # Need to remove last comma


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
            self.progress = 0
            return
        sub = list(info.split(","))
        self.reward = int(sub[0])
        self.minimum = int(sub[1])
        self.months = int(sub[2])
        self.progress = 0
        """
        This is the return on spending for the "else" category, must be set
        by with CPP. It defaults to 1.0 for CPP for cash back cards, needs
        to be updated for points.
        """
        if self.get_minimum_spend() == 0:
            self.deactivate_sign_up_bonus()
        else:
            self.ROS = (self.get_reward() * 1.0) / self.get_minimum_spend()
        if self.minimum == 0:
            self.active = False
        else:
            self.active = True

    def set_return_on_spend(self, cpp):
        """
        This sets/updates the return on spend for this card's sign-up bonus.
        :param cpp: is the cents per point on this card
        :return: none
        """
        self.ROS = (self.get_reward() * .01 * cpp) / self.get_minimum_spend()

    def get_return_on_spend(self):
        """
        This gives the user the return on spend for the SUB.
        :return: the float value for the return on spend for this SUB
        """
        return self.ROS

    def set_progress(self, progress):
        """
        This sets/updates the progress of a user's ability to get a sign-up
        bonus.
        :param progress: is the additional purchases in USD.
        :return: none
        """
        self.progress += progress
        if (self.progress >= self.minimum):
            self.deactivate_sign_up_bonus()

    def deactivate_sign_up_bonus(self):
        """
        This deactivates the sign-up bonus if the user hit the spend
        requirement or ran out of time.
        :return:
        """
        self.active = False

    def check_active(self):
        """
        This just checks if the sign_up_bonus is active or not.
        :return: True or False, depending on the the activity of the SUB.
        """
        return self.active

    def get_months(self):
        """
        This gives the user the number of months left on the sign_up_bonus.
        :return: the int value for the number of months left on this SUB.
        """
        return self.months

    def get_reward(self):
        """
        :return: the reward for this sign up bonus.
        """
        return self.reward

    def get_progress(self):
        """
        :return: the progress towards the minimum spend for this SUB
        """
        return self.progress

    def get_minimum_spend(self):
        """
        :return: the minimum spending requirement for this sSUB.
        """
        return self.minimum
