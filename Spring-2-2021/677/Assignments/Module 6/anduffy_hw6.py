"""
Aidan Duffy
Class: CS 677 - Spring 2
Date: 04/21/2021
Homework Assignment #6
Description of Problem (just a 1-2 line summary!): This is the program file
containing all methods for assignment 6.
"""
#Remainder 2(last digit of BUID is 8): R=2: class L = 1(-) and L = 3(+)
import os
import random

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def get_df(q3):
    here = os.path.abspath(__file__)
    input_dir = os.path.abspath(os.path.join(here, os.pardir))
    data_file = r"seeds_dataset.txt"
    data_file = os.path.join(input_dir, data_file)
    df = pd.read_csv(data_file, delimiter="\t+", header = None,
                     names = ["Area",'Perimeter','Compactness','Legnth',
                            'Width','Asymmetry','Groove-Length', 'L'])
    if q3 is False:
        df = df[df['L'] != 2]
    return df

def question1(data):
    print("QUESTION ONE:\n\n")
    X = data[["Area",'Perimeter','Compactness','Legnth', 'Width','Asymmetry',
              'Groove-Length']].values
    Y = data[['L']].values
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.5,
                                                        random_state=400)
    kernels = ['linear', 'rbf', 'poly']
    for k in kernels:
        svm_classifier = svm.SVC(kernel=k)
        if k == 'linear':
            print("Linear SVM:")
        elif k == 'poly':
            print("Polynomial SVM of degree = 3:")
            svm_classifier.degree = 3
        else:
            print("Gaussian SVM:")
        svm_classifier.fit(X_train,Y_train.ravel())
        pred = svm_classifier.predict(X_test)
        accuracy = metrics.accuracy_score(Y_test,pred)
        print("\tAccuracy: " + "{:.2f}%".format(accuracy * 100))
        tn, fp, fn, tp = metrics.confusion_matrix(Y_test, pred).ravel()
        tpr = tp / (tp + fn)
        tnr = tn / (fp + tn)
        print("\tTrue Negative: " + str(tn) + "\n\tFalse Positive: " + str(fp) +
              "\n\tFalse Negative: " + str(fn) + "\n\tTrue Positive: " + str(tp) +
              "\n\tTrue Positive Rate: " + "{:.2f}%".format(tpr * 100) +
              "\n\tTrue Negative Rate: " + "{:.2f}%".format(100 * tnr))
    return


def question2(data):
    print("\n" + "================================================="*2 +
          "\n\nQUESTION TWO:\n\n")
    print("kNN Classifier:")
    low_error = 1
    k_optimal = 0
    pred_optimal = []
    X = data[
        ["Area", 'Perimeter', 'Compactness', 'Legnth', 'Width', 'Asymmetry',
         'Groove-Length']].values
    Y = data[['L']].values
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.5,
                                                        random_state=400)
    for k in range(1,20):
        knn_classifier = KNeighborsClassifier(n_neighbors=k)
        knn_classifier.fit(X_train, Y_train.ravel())
        prediction = knn_classifier.predict(X_test)
        error = np.mean(prediction != Y_test)
        if error < low_error:
            low_error = error
            k_optimal = k
            pred_optimal = prediction
    accuracy = metrics.accuracy_score(Y_test, pred_optimal)
    print("\tOptimal K value is " + str(k_optimal))
    print("\tAccuracy: " + "{:.2f}%".format(accuracy * 100))
    tn, fp, fn, tp = metrics.confusion_matrix(Y_test, pred_optimal).ravel()
    tpr = tp / (tp + fn)
    tnr = tn / (fp + tn)
    print("\tTrue Negative: " + str(tn) + "\n\tFalse Positive: " + str(fp) +
          "\n\tFalse Negative: " + str(fn) + "\n\tTrue Positive: " + str(tp) +
          "\n\tTrue Positive Rate: " + "{:.2f}%".format(tpr * 100) +
          "\n\tTrue Negative Rate: " + "{:.2f}%".format(100 * tnr))
    return


def question3(data):
    #PART ONE
    k_nums = [1,2,3,4,5,6,7,8]
    features = ["Area", 'Perimeter', 'Compactness', 'Legnth', 'Width',
                'Asymmetry','Groove-Length']
    X = data[features].values
    Y = data[['L']].values
    inertia = list()
    centers = list()
    for k in k_nums:
        kmeans_class = KMeans(n_clusters=k, random_state=400)
        kmeans_class.fit(X)
        inertia.append(kmeans_class.inertia_)
    plt.plot(k_nums, inertia, "rx-")
    plt.xlabel('K')
    plt.ylabel('Distortion')
    plt.title('Q3.1: Knee Method showing optimal k value')
    plt.show()
    optimal_k = 4
    print("Given my analysis of the plot, the optimal K is " + str(optimal_k))
    #PART TWO
    feature1 = random.choice(features)
    feature2 = random.choice(features)
    while(feature1 == feature2):
        feature1 = random.choice(features)
    data2 = get_df(False)#Using groups from Q1 as mentioned in lecture
    X2 = data2[[feature1,feature2]].values
    Y2 = data2[['L']].values
    kmeans_class = KMeans(n_clusters=optimal_k, random_state=400)
    y2_means = kmeans_class.fit_predict(X2)
    plt.scatter(X2[y2_means == 0, 0], X2[y2_means == 0, 1], s=100, c='red',
                label='Cluster 1')
    plt.scatter(X2[y2_means == 1, 0], X2[y2_means == 1, 1], s=100, c='blue',
                label='Cluster 2')
    plt.scatter(X2[y2_means == 2, 0], X2[y2_means == 2, 1], s=100, c='green',
                label='Cluster 3')
    plt.scatter(X2[y2_means == 3, 0], X2[y2_means == 3, 1], s=100, c='orange',
                label='Cluster 4')
    plt.scatter(kmeans_class.cluster_centers_[:, 0],
                kmeans_class.cluster_centers_[:, 1],
                s=300, c='yellow', label='Centroids')
    plt.title('Question 3.2, optimal k is ' + str(optimal_k))
    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.show()
    #PART THREE
    label_counts = [[0,0],[0,0],[0,0],[0,0]]
    for i in range(len(X2)):
        current_centroid = y2_means[i]
        if Y2[i] == 1:
            label_counts[current_centroid][0] += 1
        else:
            label_counts[current_centroid][1] += 1
    C_list = list()
    for i in range(optimal_k):
        if label_counts[i][0] > label_counts[i][1]:
            C_list.append(1)
        else:
            C_list.append(3)
    j = 0
    print("Below are the centroid coordinates and associated label")
    for centroid in kmeans_class.cluster_centers_:
        print("\tCentroid: " + "{:.2f}".format(centroid[0]) + ", " +
              "{:.2f}".format(centroid[1]))
        print("\tLabel: " + str(C_list[j]))
        j += 1
    #PART FOUR

    return


def main():
    #data = get_df(False)
    #question1(data)
    #question2(data)
    data = get_df(True)
    question3(data)
    return


if __name__ == '__main__':
    main()