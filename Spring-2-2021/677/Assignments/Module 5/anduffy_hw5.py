"""
Aidan Duffy
Class: CS 677 - Spring 2
Date: 04/20/2021
Homework Assignment #2
Description of Problem (just a 1-2 line summary!): This is the program file
containing all methods for assignment 5.
"""
#Group 3: MSTV, Width, Mode, Variance
import os
import matplotlib.pyplot as plt
import pandas
import pandas as pd
import numpy as np
import sklearn
from sklearn.ensemble._forest import RandomForestClassifier
from sklearn.metrics._classification import confusion_matrix
from sklearn.model_selection._split import train_test_split
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing._label import LabelEncoder


def question1():
    here = os.path.abspath(__file__)
    input_dir = os.path.abspath(os.path.join(here, os.pardir))
    data_file = r"cardiotocography_data_set.xls"
    data_file = os.path.join(input_dir, data_file)
    data = pd.read_excel(data_file, sheet_name='Raw Data')
    nsp = list()
    for i in range(data.shape[0]):
        if data['NSP'][i] != 1:
            nsp.append(0)
        else:
            nsp.append(1)
    data['NSP'] = nsp
    return data


def question2(data,group_cols):
    X = data[group_cols].values[1:-3]
    le = LabelEncoder()
    Y = le.fit_transform(data[['NSP']].values[1:-3])
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.5,
                                                        random_state=500)
    NB_classifier = GaussianNB().fit(X_train,Y_train)
    pred = NB_classifier.predict(X_train)
    error_rate = np.mean(pred != Y_train)
    print("\tError Rate: " + "{:.2f}%".format(error_rate*100))
    tn, fp, fn, tp = confusion_matrix(Y_test,pred).ravel()
    tpr = tp/(tp+fn)
    tnr = tn/(fp+tn)
    print("\tTrue Negative: " + str(tn) + "\n\tFalse Positive: " + str(fp) +
          "\n\tFalse Negative: " + str(fn) + "\n\tTrue Positive: " + str(tp) +
          "\n\tTrue Positive Rate: " + "{:.2f}%".format(tpr*100) +
          "\n\tTrue Negative Rate: " + "{:.2f}%".format(100*tnr))
    return


def question3(data,group_cols):
    X = data[group_cols].values[1:-3]
    le = LabelEncoder()
    Y = le.fit_transform(data[['NSP']].values[1:-3])
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.5,
                                                        random_state=500)
    dec_tree = tree.DecisionTreeClassifier(criterion='entropy', max_features=4)
    dec_tree = dec_tree.fit(X_train,Y_train)
    pred = dec_tree.predict(X_test)
    error_rate = np.mean(pred != Y_test)
    print("\tError Rate: " + "{:.2f}%".format(error_rate * 100))
    tn, fp, fn, tp = confusion_matrix(Y_test, pred).ravel()
    tpr = tp / (tp + fn)
    tnr = tn / (fp + tn)
    print("\tTrue Negative: " + str(tn) + "\n\tFalse Positive: " + str(fp) +
          "\n\tFalse Negative: " + str(fn) + "\n\tTrue Positive: " + str(tp) +
          "\n\tTrue Positive Rate: " + "{:.2f}%".format(tpr * 100) +
          "\n\tTrue Negative Rate: " + "{:.2f}%".format(100 * tnr))
    return


def question4(data,group_cols):
    X = data[group_cols].values[1:-3]
    le = LabelEncoder()
    Y = le.fit_transform(data[['NSP']].values[1:-3])
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.5,
                                                        random_state=500)
    graph_df = pandas.DataFrame(columns=['Error Rate', 'N', 'd'])
    min_error = 1
    min_N = -1
    min_d = -1
    min_pred = []
    errors, Ns, ds= list(), list(), list()
    for N in range(1,11):
        for d in range(1,6):
            forest = RandomForestClassifier(n_estimators=N, max_depth=d,
                                            criterion='entropy')
            forest.fit(X_train,Y_train)
            pred = forest.predict(X_test)
            error_rate = np.mean(pred != Y_test)
            if error_rate < min_error:
                min_error = error_rate
                min_d = d
                min_N = N
                min_pred = pred
            errors.append(error_rate)
            Ns.append(N)
            ds.append(d)
    graph_df['Error Rate'] = errors
    graph_df['N'] = Ns
    graph_df['d'] = ds
    for i in range(1,6):
        temp = graph_df[graph_df['d'] == i]
        ploty = temp[['Error Rate']]
        plotx = temp[['N']]
        plt.plot(plotx,ploty, label = "max-depth = " + str(i))
    #plt.legend()
    #plt.show()
    print("\tBest combination is N = " + str(min_N) + ", d = " + str(min_d))
    print("\tMin Error Rate: "
          + "{:.2f}%".format(min_error * 100))
    tn, fp, fn, tp = confusion_matrix(Y_test, min_pred).ravel()
    tpr = tp / (tp + fn)
    tnr = tn / (fp + tn)
    print("\tTrue Negative: " + str(tn) + "\n\tFalse Positive: " + str(fp) +
          "\n\tFalse Negative: " + str(fn) + "\n\tTrue Positive: " + str(tp) +
          "\n\tTrue Positive Rate: " + "{:.2f}%".format(tpr * 100) +
          "\n\tTrue Negative Rate: " + "{:.2f}%".format(100 * tnr))
    return


def main():
    dataframe = question1()
    cols = ['MSTV', 'Width', 'Mode', 'Variance']
    print("Naive Bayseian Classifier Data:")
    question2(dataframe,cols)
    #print("Decision Tree Data:")
    #question3(dataframe,cols)
    #print("Random Forest Data:")
    #question4(dataframe, cols)
    return


if __name__ == '__main__':
    main()