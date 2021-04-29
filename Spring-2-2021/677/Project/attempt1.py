"""
Author: Aidan Duffy
Creation Date: April 10, 2021
Last Updated: April 10, 2021
Description: This is the first attempt at the main program file for the Movie
Recommender system. I wanted to illustrate changes over time. This one needs
to process all of the data each time, so it is slower. Also, I found the
recommendations were not always good (ie The 40 Year Old Virgin was recommended
to people who liked Toy Story).
"""
import os
import pandas as pd
from sklearn import *
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def parse_files(input_dir):
    dfs = list()
    file_names = [r"tags",r"movies",r"ratings_small",r"links_small",
                  r"genome-tags",r"genome-scores", r'credits',
                  r"movies_metadata"]
    for file in file_names:
        df = pd.read_csv(os.path.join(input_dir, file + ".csv"), delimiter=",")
        dfs.append(df)
    tf_vect = TfidfVectorizer(stop_words='english') #Elminate all the generic words
    dfs[7]['overview'] = dfs[7]['overview'].fillna('') #Replaces all null entries with the empty string
    tf_matrix = tf_vect.fit_transform(dfs[7]['overview']) #Transform and fit our data into this matrix
    return dfs, tf_matrix


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
    dataframes, movie_meta_matrix = parse_files(input_dir)
    movie_meta = dataframes[7]
    indices = pd.Series(movie_meta.index,
                        index=movie_meta['title']).drop_duplicates()
    sim_matrix = linear_kernel(movie_meta_matrix, movie_meta_matrix)
    title = 'Toy Story'
    x = content_based_recommender(title,movie_meta, indices, sim_matrix)
    print(x)
    return


if __name__ == '__main__':
    main()