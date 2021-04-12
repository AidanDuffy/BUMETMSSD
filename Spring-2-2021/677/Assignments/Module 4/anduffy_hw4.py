"""
Aidan Duffy
Class: CS 677 - Spring 2
Date: 04/13/2021
Homework Assignment #2
Description of Problem (just a 1-2 line summary!): This is the program file
containing all methods for assignment 4.
"""
import os

import matplotlib
import pandas
import pandas as pd
import math
import seaborn
from sklearn . preprocessing import StandardScaler, LabelEncoder
from sklearn . neighbors import KNeighborsClassifier
from sklearn . model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

def question1(data):
    df_0 = data[data['DEATH_EVENT'] == 0]
    df_0 = df_0[['creatinine_phosphokinase','serum_creatinine','serum_sodium',
                 'platelets']]
    df_1 = data[data['DEATH_EVENT'] == 1]
    df_1 = df_1[['creatinine_phosphokinase', 'serum_creatinine','serum_sodium',
                 'platelets']]
    matrix_0 = df_0.corr()
    matrix_1 = df_1.corr()
    seaborn.heatmap(matrix_0,annot = True)
    plt.show()
    seaborn.heatmap(matrix_1,annot = True)
    plt.show()
    return


def question2(data):
    #Group 3: X: serum sodium, Y: serum creatinine
    X = np.array(data['serum_sodium'])
    Y = np.array(data['serum_creatinine'])
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.5,
                                                        random_state=100)
    for deg in range(1,4):
        weights = np.polyfit(X_train,Y_train,deg)
        model = np.poly1d(weights)
        predicted = model(X_test)
        rmse = np.sqrt(mean_squared_error(Y_test,predicted))
        r2 = r2_score(Y_test,predicted)
        print("For polynomial of degree " + "{:.0f}".format(deg))
        weight_str = ""
        for w in weights:
            weight_str += "{:.2f}".format(w) + ", "
        print("Weights: " + weight_str)
        print("R Mean Squared Error: " + "{:.2f}".format(rmse))
        print("R2: " + "{:.2f}".format(r2))
        matplotlib.pyplot.scatter(X_test,Y_test,c='green')
        matplotlib.pyplot.scatter(X_test, predicted, c='red')
        matplotlib.pyplot.show()
        loss = 0
        for i in range(len(Y_test)):
            loss += (Y_test[i] - predicted[i])**2
        print("Estimated Loss: " + "{:.2f}".format(loss) + "\n\n")
    question2_logs(X_train, X_test, Y_train, Y_test)
    return


def question2_logs(X_train, X_test, Y_train, Y_test):
    deg = 1
    weights = [np.polyfit(np.log(X_train), Y_train, deg),
               np.polyfit(np.log(X_train), np.log(Y_train), deg)]
    for weight in weights:
        model = np.poly1d(weight)
        predicted = model(np.log(X_test))
        if deg == 2:
            Y_test = np.log(Y_test)
        rmse = np.sqrt(mean_squared_error(Y_test, predicted))
        r2 = r2_score(Y_test, predicted)
        print("For logarithm (type " + str(deg) + "):")
        deg += 1
        weight_str = ""
        for w in weight:
            weight_str += "{:.2f}".format(w) + ", "
        print("Weights: " + weight_str)
        print("R Mean Squared Error: " + "{:.2f}".format(rmse))
        print("R2: " + "{:.2f}".format(r2))
        matplotlib.pyplot.scatter(X_test, Y_test, c='green')
        matplotlib.pyplot.scatter(X_test, predicted, c='red')
        matplotlib.pyplot.show()
        loss = 0
        for i in range(len(Y_test)):
            loss += (Y_test[i] - predicted[i]) ** 2
        print("Estimated Loss: " + "{:.2f}".format(loss) + "\n\n")
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
    print("For survivors:\n")
    question2(data[data['DEATH_EVENT'] == 0]) #Survivors
    print("=======================\nFor deceased:\n")
    question2(data[data['DEATH_EVENT'] == 1]) #Deceased



if __name__ == '__main__':
    main()