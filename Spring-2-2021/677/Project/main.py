"""
Author: Aidan Duffy
Creation Date: April 10, 2021
Last Updated: April 10, 2021
Description: This is the main program file for the Movie Recommender system.
"""
import os
import pandas as pd
from sklearn import *
import numpy as np
import movie
import user


def parse_files(input_dir):
    dfs = list()
    file_names = [r"tags",r"movies",r"ratings",r"links",r"genome-tags",
                  r"genome-scores"]
    for file in file_names:
        df = pd.read_csv(os.path.join(input_dir, file + ".csv"), delimiter=",")
        dfs.append(df)
    return dfs


def set_title_and_year(movies):
    titles, years = list(),list()
    for i in range(movies.shape[0]):
        current_title = movies["title"][i]
        titles.append(current_title[:-6])
        years.append(current_title[-5:-1])
    movies['title'] = titles
    movies['year'] = years
    return movies

def add_average_rating(dfs):
    movies = dfs[1]
    movies = set_title_and_year(movies)
    reviews = dfs[2]
    rating_list = ["N/A"]*movies.shape[0]
    raw_scores = ["N/A"] * movies.shape[0]
    review_count = ["N/A"] * movies.shape[0]
    ratings = reviews.groupby('movieId', as_index=False)['rating'].mean()
    count = 0
    for i in (ratings['movieId']):
        current_rating = ratings[ratings['movieId'] == i]['rating']
        current_rating = 2*current_rating[count]
        raw_scores[count] = current_rating
        current_rating = float("{:.1f}".format(2*current_rating)) #2x so its 10pt scale
        rating_list[count] = current_rating
        review_count[count] = reviews.loc[reviews.movieId == i,
                                          'movieId'].count()
        count += 1
    movies['average-rating'] = rating_list
    movies['scores'] = raw_scores
    movies['number-of-ratings'] = review_count
    print("DONE")
    return movies


def weight_rating(data):
    return


def main():
    here = os.path.abspath(__file__)
    input_dir = os.path.abspath(os.path.join(here, os.pardir + r"/Data"))
    dataframes = parse_files(input_dir)
    movies_df = add_average_rating(dataframes)
    movies_df.to_csv(os.path.join(input_dir, r"moviesWithRatingAverage.csv"))
    dataframes[1] = pd.read_csv(os.path.join(input_dir,
                                r"moviesWithRatingAverage.csv"), low_memory=False)
    movies_df = dataframes[1]
    movies_df = movies_df[movies_df.columns.values[1:]]
    movies_df = set_title_and_year(movies_df)
    return


if __name__ == '__main__':
    main()