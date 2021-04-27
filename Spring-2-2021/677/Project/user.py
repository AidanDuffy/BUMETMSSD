"""
Author: Aidan Duffy
Creation Date: April 10, 2021
Last Updated: April 10, 2021
Description: This class is for the user, storing their relevant info and
ratings.
"""


class User:

    def __init__(self, userid,movies = dict()):
        self.id = userid
        self.movies = movies

    def add_rating(self,movie, rating):
        self.movies[movie] = rating

    def get_ratings(self):
        return self.movies

    def get_userid(self):
        return self.id
