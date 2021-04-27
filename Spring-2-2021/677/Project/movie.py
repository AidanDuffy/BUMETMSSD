"""
Author: Aidan Duffy
Creation Date: April 10, 2021
Last Updated: April 10, 2021
Description: This class is for the movie, storing the relevant info.
"""


class Movie:

    def __init__(self, title_and_year, id, genres):
        self.title, self.year = self.set_title_and_year(title_and_year)
        self.id = id
        genre_list = genres.split("|")
        self.genres = genre_list

    def set_title_and_year(self, title_and_year):
        title = title_and_year[:-6]
        year = title_and_year[-5:-1]
        return title,year
