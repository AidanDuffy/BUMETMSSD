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
    x_train = data.sample(frac=.5)
    x_test = data.drop(x_train.index)
    seaborn.pairplot(x_train,hue='Color')
    seaborn.pairplot(x_train[x_train['Color'] == 'red'])
    seaborn.pairplot(x_train[x_train['Color'] == 'green'])
    x_test_classifier_labels = []
    for i in range(x_test.shape[0]):
        if (float(x_test['Variance'][i]) > -4) \
                and (float(x_test['Skewness'][i]) > 5)\
                and float(x_test['Kurtosis'][i]) < 0:
            x_test_classifier_labels.append("good")
        else:
            x_test_classifier_labels.append("fake")
    x_test["Predicted"] = x_test_classifier_labels
    return


def question3():
    return


def question4():
    return


def question5():
    return


def question6():
    return


def main():
    input_dir = r'G:\Documents\BUMETMSSD\Spring-2-2021\677\Assignments'
    input_dir += r'\Module 3'
    file_name = 'data_banknote_authentication.txt'
    banknote_data = os.path.join(input_dir,  file_name)
    banknote_df = pd.read_csv(banknote_data, delimiter=",")
    banknote_df = question1(banknote_df)
    banknote_df = question2(banknote_df)



if __name__ == '__main__':
    main()