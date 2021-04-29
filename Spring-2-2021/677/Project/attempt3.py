"""
Author: Aidan Duffy
Creation Date: April 10, 2021
Last Updated: April 21, 2021
Description: This is the third attempt at the main program file for the Movie
Recommender system. I successfully was able to implement a weighted rating system
as well as display the top X films that are in the top Xth percentile in terms
of popularity(votes cast on imdb).
"""
import math
import os
import string

import pandas
import pandas as pd
from sklearn import *
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import unicodedata

movies_df_index = 0
movies_metadata_df_index = 1


def parse_files(input_dir):
    dfs = list()
    file_names = [r"tags",r"movies",r"ratings_small",r"links_small",
                  r"genome-tags",r"genome-scores", r'credits',
                  r"movies_metadata"]
    used_files = [file_names[1], file_names[7]]
    for file in used_files:
        df = pd.read_csv(os.path.join(input_dir, file + ".csv"), delimiter=",")
        dfs.append(df)
    # Elminate all the generic words
    tf_vect = TfidfVectorizer(stop_words='english')
    # Replaces all null entries with the empty string
    dfs[movies_metadata_df_index]['overview'] = \
        dfs[movies_metadata_df_index]['overview'].fillna('')
    # Transform and fit our data into this matrix
    tf_matrix = tf_vect.fit_transform(dfs[movies_metadata_df_index]['overview'])
    return dfs[0],dfs[1], tf_matrix


def format_titles(title1, title2):
    stop = ["the",'The', "a",'A', 'an', 'An', "Les", "La"]
    title1 = title1.str.replace('[{}]'.format(string.punctuation), '')
    title2 = title2.str.replace('[{}]'.format(string.punctuation), '')
    new_title1 = list()
    count = 0
    for title in title1:
        if title is None or title != title:
            continue
        words = title.split()
        if words[0] in stop:
            words = words[1:]
        final_title = " ".join(words)
        new_title1.append(final_title)
        count += 1
    return new_title1,title2


def remove_accents(title):
    nfkd_form = unicodedata.normalize('NFKD', title)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def fix_years_add_movie_id(metadata, movies):
    years,ids = list(), list()
    metadata_index = 0
    meta_titles_df = metadata["title"]
    movie_titles_df = movies["title"]
    meta_titles_df,movie_titles_df=format_titles(meta_titles_df,movie_titles_df)
    for i in range(movies.shape[0]):
        meta_title = meta_titles_df[metadata_index].lower().replace(" ", "")
        current_title = movie_titles_df[i]
        year = current_title[-4:]
        current_title = current_title[:-5].lower().replace(" ", "")
        current_title = remove_accents(current_title)
        if meta_title in current_title:
            years.append(year)
            ids.append(movies['movieId'][i])
            metadata_index += 1
    metadata['movieId'] = ids
    metadata['year'] = years
    return metadata


def calculate_weighted_rating(df, min, avg):
    """
    IMDB's formula for calculated a weighted rating.
    :param df: The movie metadata dataframe.
    :param min: the minimum number of votes to be considered
    :param avg: the average vote score
    :return: the weight rating.
    """
    average_rating = df['vote_average']
    vote_count = df['vote_count']
    denominator = min + vote_count
    weighted_rating = ((vote_count / denominator) * average_rating) \
                      + ((min / denominator) * avg)
    return weighted_rating


def weighted_rating(movie_data,percentile = 0.9):
    """
    This will help create a top X% chart of movies.
    :param movie_data:
    :return:
    """
    mean_vote = movie_data['vote_average'].mean()
    min_vote = movie_data['vote_count'].quantile(percentile)
    print("\n\nFor the entered percentile(" + str(100*percentile) + ") the film " +
        "requires at least " + str(round(min_vote)) + " votes.\n")
    top_x_percent=movie_data.copy().loc[movie_data['vote_count']>=min_vote]
    top_x_percent['weighted_score'] = top_x_percent.apply(
        calculate_weighted_rating,axis =1, args = (min_vote,mean_vote))
    top_x_percent = top_x_percent.sort_values('weighted_score',
                                                        ascending=False)
    return top_x_percent


def content_based_recommender(title, metadata,indices, sim_scores):
    idx = indices[title]
    sim_scores = list(enumerate(sim_scores[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return metadata['title'].iloc[movie_indices]


def main():
    here = os.path.abspath(__file__)
    input_dir = os.path.abspath(os.path.join(here, os.pardir + r"/Data"))
    movies, movie_meta, movie_meta_matrix = parse_files(input_dir)
    #movie_meta = fix_years_add_movie_id(movie_meta,movies)
    indices = pd.Series(movie_meta.index,
                        index=movie_meta['title']).drop_duplicates()
    percentile_q = "What percentile, in terms of votes received, would you " \
                   "like to see the top films for?\nEx: 25th percentile only " \
                    "needs 3 votes, but 90th needs 160 and 95th needs " \
                    "over 400!\nEnter as a float, so \'0.90\' for the 90th" \
                    " percentile: "
    top_x = "How many popular films would you like displayed? Top 20? 50?" \
            "(Enter a valid int below 500 and above 0): "
    while True:
        try:
            percentile = float(input(percentile_q))
            top_num = int(input(top_x))
            if top_num < 500 and top_num > 0:
                break
            else:
                print("Invalid integer!")
        except:
            print("Enter a valid number!")
    top_x_percent = weighted_rating(movie_meta,percentile)
    print(top_x_percent[['title','vote_count','vote_average','weighted_score']].head(top_num))
    #sim_matrix = linear_kernel(movie_meta_matrix, movie_meta_matrix)
    #title = 'Toy Story'
    #x = content_based_recommender(title,movie_meta, indices, sim_matrix)
    #print(x)
    return


if __name__ == '__main__':
    main()