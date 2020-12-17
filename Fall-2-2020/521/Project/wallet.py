"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 15, 2020
Final Project
Description: This is a user-defined class, as requested in the project
guidelines that is for the creation of wallet objects.
"""

import credit_card

class Wallet:

    __main_categories = ["dining","grocery","travel", "transit", "gas",
                        "online shopping", "else", "drugstores", "Amazon",
                         "PayPal"]

    def __init__(self):
        self.cards = list()
        self.best = self.construct_best_for_category()


    def construct_best_for_category(self):
        """
        This constructs a new empty best category wallet
        :return: the new best for category dictionary
        """
        best = dict()
        for category in Wallet.__main_categories:
            best[category] = None
        return best


    def add_card(self, card):
        """
        This adds a new card to the wallet
        :param card: the new card
        :return: none
        """
        self.cards.append(card)
        self.__check_if_new_best(card)

    def find_best_for_category(self, category):
        """
        Given a category, it'll return the best card
        :param category: the given category
        :return: the card that is best for that category
        """
        return self.best[category]

    def __check_if_new_best(self, card):
        """
        This takes in a new card and checks if it is now the best in any
        category
        :param card: is the new card
        :return: none
        """
        for category in self.best.keys():
            current_card = self.find_best_for_category(category)
            if current_card is None:
                self.best[category] = card
            else:
                current_card_value = current_card.check_categories(category)
                added_card_value = card.check_categories(category)
                if added_card_value > current_card_value:
                    self.best[category] = card

