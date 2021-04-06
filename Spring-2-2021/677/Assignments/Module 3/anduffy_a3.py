"""
Aidan Duffy
Class: CS 677 - Spring 2
Date: 04/06/2021
Homework Assignment #2
Description of Problem (just a 1-2 line summary!): This is the program file
containing all methods for assignment 3.
"""
import os
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
    color_list = []
    sum_total = {"Variance":0,"Skewness":0,"Kurtosis":0,"Entropy":0}
    std_total = {"Variance": 0, "Skewness": 0, "Kurtosis": 0, "Entropy": 0}
    sum_green = {"Variance":0,"Skewness":0,"Kurtosis":0,"Entropy":0}
    std_green = {"Variance": 0, "Skewness": 0, "Kurtosis": 0, "Entropy": 0}
    greens = 0
    sum_red = {"Variance":0,"Skewness":0,"Kurtosis":0,"Entropy":0}
    std_red = {"Variance": 0, "Skewness": 0, "Kurtosis": 0, "Entropy": 0}
    reds = 0
    for i in range(data.shape[0]):
        if int(data['Class'][i]) == 0:
            color_list.append('green')
            for j in sum_total.keys():
                sum_green[j] += float(data[j][i])
            greens += 1
        else:
            color_list.append('red')
            for j in sum_total.keys():
                sum_red[j] += float(data[j][i])
            reds += 1
        for k in sum_total.keys():
            sum_total[k] += float(data[k][i])
    data['Color'] = color_list
    for x in sum_total.keys():
        sum_total[x] = sum_total[x]/(greens+reds)
        sum_red[x] = sum_red[x] / (reds)
        sum_green[x] = sum_green[x] / (greens)
    for i in range(data.shape[0]):
        if int(data['Class'][i]) == 0:
            for j in sum_total.keys():
                std_green[j] += (float(data[j][i])-sum_green[x])**2
            greens += 1
        else:
            for j in sum_total.keys():
                std_red[j] += (float(data[j][i])-sum_red[x])**2
            reds += 1
        for k in sum_total.keys():
            std_total[k] += (float(data[j][i])-sum_total[x])**2
    for x in sum_total.keys():
        std_total[x] = math.sqrt(std_total[x]/(greens+reds))
        std_red[x] = math.sqrt(std_red[x] / (reds))
        std_green[x] = math.sqrt(std_green[x] / (greens))
    print("Class 0:\nAverages:\n" + str(sum_green) + "\nStandard Deviations"
                                                     ":\n"+str(std_green))
    print("Class 1:\nAverages:\n" + str(sum_red) + "\nStandard Deviations"
                                                     ":\n" + str(std_red))
    print("All:\nAverages:\n" + str(sum_total) + "\nStandard Deviations"
                                                     ":\n" + str(std_total))
    return data


def question2(data):
    x_train,x_test = train_test_split(data,test_size=.5, random_state=0)
    #seaborn.pairplot(x_train,hue='Color')
    #seaborn.pairplot(x_train[x_train['Color'] == 'red'])
    #seaborn.pairplot(x_train[x_train['Color'] == 'green'])
    x_test_classifier_labels = []
    for i in range(data.shape[0]):
        try:
            if (float(x_test['Variance'][i]) > 0) \
                    and (float(x_test['Skewness'][i]) > 5)\
                    and float(x_test['Kurtosis'][i]) > 0:
                x_test_classifier_labels.append("good")
            else:
                x_test_classifier_labels.append("fake")
        except:
            continue
    x_test["Predicted"] = x_test_classifier_labels
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for i in range(data.shape[0]):
        try:
            if x_test['Color'][i] == 'red':
                if x_test["Predicted"][i] == 'fake':
                    tn += 1
                else:
                    fp += 1
            else:
                if x_test["Predicted"][i] == 'fake':
                    fn += 1
                else:
                    tp += 1
        except:
            continue
    tpr = tp/(tp+fn)
    tnr = tn/(tn+fp)
    accuracy = (tp+tn)/(tp+tn+fp+fn)
    print("Prediction Accuracies:\n\tTrue Positives: " + str(tp) +
          "\n\tFalse Positives: " + str(fp) + "\n\tTrue Negatives: "+ str(tn)+
          "\n\tFalse Negatives: " + str(fn) + "\n\tTrue Positive Rate: " +
          str(tpr) + "\n\tTrue Negative Rate: " + str(tnr) + "\n\tAccuracy: " +
          str(accuracy))
    return


def question3(data):
    k_nums = [3,5,7,9,11]
    X = data[["Variance", "Skewness", "Kurtosis","Entropy"]].values
    scaler = StandardScaler().fit(X)
    X = scaler.transform(X)
    Y = LabelEncoder().fit_transform(data[["Color"]].values)
    x_train, X_test, y_train, Y_test = train_test_split(X,Y,
                                                test_size=.5, random_state=0)
    error_rate = []
    low_error = 1
    k_optimal = 0
    for k in k_nums:
        knn_classifier = KNeighborsClassifier(n_neighbors=k)
        knn_classifier.fit(x_train,y_train)
        prediction = knn_classifier.predict(X_test)
        error = np.mean(prediction != Y_test)
        error_rate.append(error)
        if error < low_error:
            low_error = error
            k_optimal = k
    plt.plot(k_nums, error_rate, color='red', linestyle='dashed',
             marker='o', markerfacecolor='black', markersize=10)
    plt.title('Error Rate vs. k')
    plt.xlabel('number of neighbors : k')
    plt.ylabel('Error Rate')
    plt.show()
    knn_classifier = KNeighborsClassifier(n_neighbors=k_optimal)
    knn_classifier.fit(X, Y)
    prediction = knn_classifier.predict(X_test)
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    total = 0
    for pred in prediction:
        if pred != Y_test[total]:
            if Y_test[total] == 0:
                fn += 1
            else:
                fp += 1
        else:
            if Y_test[total] == 0:
                tp += 1
            else:
                tn += 1
        total += 1
    tpr = tp/(tp+fn)
    tnr = tn/(tn+fp)
    accuracy = (tp+tn)/total
    print("k-NN Accuracies:\n\tTrue Positives: " + str(tp) +
          "\n\tFalse Positives: " + str(fp) + "\n\tTrue Negatives: " + str(
        tn) +
          "\n\tFalse Negatives: " + str(fn) + "\n\tTrue Positive Rate: " +
          str(tpr) + "\n\tTrue Negative Rate: " + str(tnr) + "\n\tAccuracy: " +
          str(accuracy))
    X_test = [[7,1,1,8]]
    knn_classifier = KNeighborsClassifier(n_neighbors=k_optimal)
    knn_classifier.fit(X, Y)
    prediction = knn_classifier.predict(X_test)
    print(prediction)
    return


def question4(data):
    k_optimal = 3
    X_sets = [data[["Skewness", "Kurtosis", "Entropy"]].values,
              data[["Variance", "Kurtosis", "Entropy"]].values,
              data[["Variance", "Skewness", "Entropy"]].values,
              data[["Variance", "Skewness", "Kurtosis"]].values]
    Y = LabelEncoder().fit_transform(data[["Color"]].values)
    error_rate =[]
    for X in X_sets:
        scaler = StandardScaler().fit(X)
        X = scaler.transform(X)
        x_train, X_test, y_train, Y_test = train_test_split(X, Y,
                                                            test_size=.5,
                                                            random_state=0)
        knn_classifier = KNeighborsClassifier(n_neighbors=k_optimal)
        knn_classifier.fit(X, Y)
        prediction = knn_classifier.predict(X_test)
        error_rate.append(np.mean(prediction != Y_test))
    print("No Variance: "+str(1-error_rate[0]))
    print("No Skewness: " + str(1-error_rate[1]))
    print("No Kurtosis: " + str(1-error_rate[2]))
    print("No Entropy: " + str(1-error_rate[3]))


def question5(data):
    X = data[["Variance", "Skewness", "Kurtosis", "Entropy"]].values
    scaler = StandardScaler().fit(X)
    X = scaler.transform(X)
    Y = LabelEncoder().fit_transform(data[["Color"]].values)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                        test_size=.5,
                                                        random_state=0)
    log_reg_classifier = LogisticRegression().fit(X_train,Y_train)
    prediction = log_reg_classifier.predict(X_test)
    accuracy = np.mean(prediction == Y_test)
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    total = 0
    for pred in prediction:
        if pred != Y_test[total]:
            if Y_test[total] == 0:
                fn += 1
            else:
                fp += 1
        else:
            if Y_test[total] == 0:
                tp += 1
            else:
                tn += 1
        total += 1
    tpr = tp / (tp + fn)
    tnr = tn / (tn + fp)
    accuracy = (tp + tn) / total
    print("\n\nLogisitic Regression Accuracies:\n\tTrue Positives: " + str(tp) +
          "\n\tFalse Positives: " + str(fp) + "\n\tTrue Negatives: " + str(
        tn) +
          "\n\tFalse Negatives: " + str(fn) + "\n\tTrue Positive Rate: " +
          str(tpr) + "\n\tTrue Negative Rate: " + str(tnr) + "\n\tAccuracy: " +
          str(accuracy))
    X_test = [[7, 1, 1, 8]]
    log_reg_classifier = LogisticRegression().fit(X_train, Y_train)
    prediction = log_reg_classifier.predict(X_test)
    print(prediction)
    return


def question6(data):
    X_sets = [data[["Skewness", "Kurtosis", "Entropy"]].values,
              data[["Variance", "Kurtosis", "Entropy"]].values,
              data[["Variance", "Skewness", "Entropy"]].values,
              data[["Variance", "Skewness", "Kurtosis"]].values]
    Y = LabelEncoder().fit_transform(data[["Color"]].values)
    error_rate = []
    for X in X_sets:
        scaler = StandardScaler().fit(X)
        X = scaler.transform(X)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                            test_size=.5,
                                                            random_state=0)
        log_reg_classifier = LogisticRegression().fit(X_train, Y_train)
        prediction = log_reg_classifier.predict(X_test)
        error_rate.append(np.mean(prediction != Y_test))
    print("No Variance: " + str(1 - error_rate[0]))
    print("No Skewness: " + str(1 - error_rate[1]))
    print("No Kurtosis: " + str(1 - error_rate[2]))
    print("No Entropy: " + str(1 - error_rate[3]))
    return


def main():
    input_dir = r'G:\Documents\BUMETMSSD\Spring-2-2021\677\Assignments'
    input_dir += r'\Module 3'
    file_name = 'data_banknote_authentication.txt'
    banknote_data = os.path.join(input_dir,  file_name)
    banknote_df = pd.read_csv(banknote_data, delimiter=",")
    banknote_df = question1(banknote_df)
    question2(banknote_df)
    #question3(banknote_df)
    question4(banknote_df)
    #question5(banknote_df)
    question6(banknote_df)



if __name__ == '__main__':
    main()