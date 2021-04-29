"""
Author: Aidan Duffy
Creation Date: April 10, 2021
Last Updated: April 15, 2021
Description: This is the second attempt at the main program file for the Movie
Recommender system. I filtered out some of the data at the start to prevent
wasted time. I also attempted to add the movieId and years properly to the main
metadata file, but struggled there.
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


def calculate_weighted_rating(movie_data):
    weighted_ratings = pandas.DataFrame()


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
    sim_matrix = linear_kernel(movie_meta_matrix, movie_meta_matrix)
    title = 'Toy Story'
    x = content_based_recommender(title,movie_meta, indices, sim_matrix)
    print(x)
    return


if __name__ == '__main__':
    main()