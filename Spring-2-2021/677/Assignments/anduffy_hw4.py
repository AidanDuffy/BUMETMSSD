"""
Aidan Duffy
Class: CS 677 - Spring 2
Date: 04/13/2021
Homework Assignment #2
Description of Problem (just a 1-2 line summary!): This is the program file
containing all methods for assignment 4.
"""
import os

import pandas
import pandas as pd
import math
import seaborn
from sklearn . preprocessing import StandardScaler, LabelEncoder
from sklearn . neighbors import KNeighborsClassifier
from sklearn . model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

def question1(data):
    df_0 = data[data['DEATH_EVENT'] == 0]
    df_1 = data[data['DEATH_EVENT'] == 1]
    matrix_0 = df_0.corr()
    matrix_1 = df_1.corr()
    return data


def question2(data):
    return


def question3(data):
    return


def main():
    here = os.path.abspath(__file__)
    input_dir = os.path.abspath(os.path.join(here,os.pardir))
    data_file = r"Module 4/heart_failure_clinical_records_dataset.csv"
    data_file = os.path.join(input_dir,data_file)
    data = pandas.read_csv(data_file)
    data = data[['creatinine_phosphokinase', 'serum_creatinine', 'serum_sodium',
                'platelets','DEATH_EVENT']]
    question1(data)



if __name__ == '__main__':
    main()