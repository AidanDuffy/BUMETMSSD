"""
Aidan Duffy
Class: CS 677 - Spring 2
Date: 03/30/2021
Homework Assignment #2
Description of Problem (just a 1-2 line summary!):
"""

import read_stock_data_from_file
import pandas as pd
import os
import numpy as np
import anduffy_q1

tickers = ['SPY', 'DB']
input_dir = r'G:\Documents\BUMETMSSD\Spring-2-2021\677\Assignments'
ticker_files = []
for ticker in tickers:
    ticker_files.append(os.path.join(input_dir, ticker + '.csv'))

#Question 1.1
def read_file_with_true_label(ticker_file):
    init_dataframe = pd.read_csv(ticker_file, delimiter=",")
    dataframe = init_dataframe
    true_vals = []
    for ret in dataframe["Return"]:
        if ret >=0:
            true_vals.append('+')
        else:
            true_vals.append('-')
    dataframe['True Value'] = true_vals
    return dataframe

#Q1.2
def odds_of_up_days(ticker_df):
    total_days = 0
    up_days = 0
    for i in range(ticker_df.shape[0]):
        if int(ticker_df['Year'][i]) > 2018:
            break
        total_days += 1
        if ticker_df['True Value'][i] == '+':
            up_days += 1
    return up_days/total_days

#Q1.3
def odds_consecutive_down_days(ticker_df):
    res = [0,0,0]
    downs = [0,0,0]
    ups = [0,0,0]
    in_a_row = 0
    for i in range(ticker_df.shape[0]):
        if int(ticker_df['Year'][i]) > 2018:
            break
        if ticker_df['True Value'][i] == '+':
            if in_a_row >= 1:
                ups[0] += 1
                downs[0] += 1
            if in_a_row >= 2:
                ups[1] += 1
                downs[1] += 1
            if in_a_row >= 3:
                ups[2] += 1
                downs[2] += 1
            in_a_row = 0
        else:
            if in_a_row >= 1:
                downs[0] += 1
            if in_a_row >= 2:
                downs[1] += 1
            if in_a_row >= 3:
                downs[2] += 1
            in_a_row += 1
    for i in range(3):
        res[i] = ups[i]/downs[i]
    return res

#Q1.4
def odds_consecutive_up_days(ticker_df):
    res = [0,0,0]
    downs = [0,0,0]
    ups = [0,0,0]
    in_a_row = 0
    for i in range(ticker_df.shape[0]):
        if int(ticker_df['Year'][i]) > 2018:
            break
        if ticker_df['True Value'][i] == '+':
            if in_a_row >= 1:
                ups[0] += 1
            if in_a_row >= 2:
                ups[1] += 1
            if in_a_row >= 3:
                ups[2] += 1
            in_a_row += 1
        else:
            if in_a_row >= 1:
                ups[0] += 1
                downs[0] += 1
            if in_a_row >= 2:
                ups[1] += 1
                downs[1] += 1
            if in_a_row >= 3:
                ups[2] += 1
                downs[2] += 1
            in_a_row += 1
            in_a_row = 0
    for i in range(3):
        res[i] = 1 - downs[i]/ups[i]
    return res


def question1(df):
    up_odds = []
    consecutive_down_odds = []
    consecutive_up_odds = []
    up_odds.append(odds_of_up_days(df))
    consecutive_down_odds = (odds_consecutive_down_days(df))
    consecutive_up_odds = (odds_consecutive_up_days(df))
    for i in range(3):
        print("There is a " + format(consecutive_down_odds[i], '.2%') +
              " chance of an up day after " + str(i + 1) + " down days")
        print("There is a " + format(consecutive_up_odds[i], '.2%') +
              " chance of an up day after " + str(i + 1) + " up days.")


def fetch_hyperparameter(df,seq,hyperparam_sequences_freq):
    seq_total = 0
    seq_up = 0
    seq_down = 0
    current = ""
    if seq in hyperparam_sequences_freq.keys():
        return hyperparam_sequences_freq[seq]
    for i in range(len(seq.split(",")) - 1, df.shape[0]):
        if int(df['Year'][i]) > 2018:
            break
        current = df['True Value'][i-1] + "," + df['True Value'][i]
        if len(seq.split(",")) > 2:
            current = df['True Value'][i-2] + "," + current
            if len(seq.split(",")) == 4:
                current = df['True Value'][i - 3] + "," + current
        if current == seq:
            seq_total += 1
            if df['True Value'][i+1] == "+":
                seq_up += 1
            else:
                seq_down += 1
    if seq_up >= seq_down:
        hyperparam_sequences_freq[seq] = "+"
        return "+"
    else:
        hyperparam_sequences_freq[seq] = "-"
        return "-"


#Q2.1
def predictive_labels(df):
    predicted = {2:[],3:[],4:[]}
    seq = ['','','']
    hyperparam_sequences_freq = dict()
    for i in range(df.shape[0]):
        if int(df['Year'][i]) <= 2018:
            for j in range(3):
                predicted[2 + j].append("")
            continue
        seq[0] = df['True Value'][i-1] + "," + df['True Value'][i]
        seq[1] = df['True Value'][i-2] + "," + seq[0]
        seq[2] = df['True Value'][i-3] + "," + seq[1]
        for j in range(3):
            predicted[2+j].append(fetch_hyperparameter(df,seq[j],
                                  hyperparam_sequences_freq))

    df["Predictive Label W2"] = predicted[2]
    df["Predictive Label W3"] = predicted[3]
    df["Predictive Label W4"] = predicted[4]
    #df.to_csv(r"G:\Documents\BUMETMSSD\Spring-2-2021\677\Assignments\SPYpredlabels.csv")

#Q2.2
def check_predictive_labels(df):
    total = [0,0,0]
    correct = [0,0,0]
    for i in range(df.shape[0]):
        if int(df['Year'][i]) <= 2018:
            continue
        for j in range(3):
            total[j] += 1
            check = "Predictive Label W" + str(2+j)
            if df[check][i] == df['True Value'][i]:
                correct[j] += 1
    result =[]
    for i in range(3):
        result.append(correct[i]/total[i])
    return result


#Q2.2
def check_predictive_labels_signs(df):
    result = {"+":[0,0,0],"-":[0,0,0]}
    total = {"+":[0,0,0],"-":[0,0,0]}
    correct = {"+":[0,0,0],"-":[0,0,0]}
    for i in range(df.shape[0]):
        if int(df['Year'][i]) <= 2018:
            continue
        for j in range(3):
            sign = df['True Value'][i]
            total[sign][j] += 1
            check = "Predictive Label W" + str(2+j)
            pred_sign = df[check][i]
            if pred_sign == sign:
                correct[sign][j] += 1
    for c in ["+","-"]:
        for i in range(3):
            result[c][i] = correct[c][i]/total[c][i]
    return result


def question2(df):
    predictive_accuracy = []
    predictive_labels(df)
    predictive_accuracy = check_predictive_labels(df)
    max_accuracy = [2, predictive_accuracy[0]]
    sign_accuracy = check_predictive_labels_signs(df)
    for i in range(3):
        if predictive_accuracy[i] > max_accuracy[1]:
            max_accuracy = [2 + i, predictive_accuracy[i]]
        print("Looking back " + str(i + 2) + " days, the predictive model "
                                             "was accurate " + format(
            predictive_accuracy[i], '.2%') +
              " of the time. For true +, the rate was "
              + format(sign_accuracy["+"][i], '.2%') + " and " +
              format(sign_accuracy["-"][i],'.2%') + " for true - values.")
    print("It was most accurate to look back " + str(max_accuracy[0]) +
          " days.")


#Q3.1
def ensemble_predictive_labels(df):
    ensemble = []
    seq = ['','','']
    for i in range(df.shape[0]):
        if int(df['Year'][i]) <= 2018:
            ensemble.append("")
            continue
        seq[0] = df["Predictive Label W2"][i]
        seq[1] = df["Predictive Label W3"][i]
        seq[2] = df["Predictive Label W4"][i]
        up_count = seq.count("+")
        if up_count > 1:
            ensemble.append("+")
        else:
            ensemble.append("-")
    df["Ensemble Value"] = ensemble


#Q3.2
def check_ensemble_labels(df):
    total_labels = 0
    correct = 0
    for i in range(df.shape[0]):
        if int(df['Year'][i]) <= 2018:
            continue
        total_labels += 1
        if df['Ensemble Value'][i] == df['True Value'][i]:
            correct += 1
    return correct/total_labels


def check_ensemble_labels_signs(df):
    total_labels = [0,0]
    correct = [0,0]
    for i in range(df.shape[0]):
        if int(df['Year'][i]) <= 2018:
            continue
        if df['True Value'][i] == "+":
            total_labels[0] += 1
            if df['Ensemble Value'][i] == "+":
                correct[0] += 1
        else:
            total_labels[1] += 1
            if df['Ensemble Value'][i] == "-":
                correct[1] += 1
    accuracy = []
    for i in range(2):
        accuracy.append(correct[i]/total_labels[i])
    return accuracy


def question3(df):
    ensemble_predictive_labels(df)
    accuracy = check_ensemble_labels(df)
    predictive_accuracy = check_predictive_labels(df)
    sign_accuracy = check_ensemble_labels_signs(df)
    pred_sign_accuracy = check_predictive_labels_signs(df)
    print("The ensemble labels were accurate " + format(accuracy, '.2%') +
          " of the time. For true +, the rate was "
              + format(sign_accuracy[0], '.2%') + " and " +
              format(sign_accuracy[1],'.2%') + " for true - values.")
    for i in range(3):
        if accuracy > predictive_accuracy[i]:
            print("The ensemble labels were more accurate than relying only"
                  " on looking back " + str(i+2) + " days.")
        else:
            print("The ensemble labels were less accurate than relying only"
                  " on looking back " + str(i + 2) + " days.")
        for j in range(2):
            sign = "+-"[j]
            if sign_accuracy[j] > pred_sign_accuracy[sign][i]:
                print(
                    "The ensemble labels were more accurate than relying only"
                    " on looking back " + str(i + 2) + " days for true " +sign)
            else:
                print(
                    "The ensemble labels were less accurate than relying only"
                    " on looking back " + str(i + 2) + " days for true " +sign)

def true_signs(df,type):
    correct = [0, 0]
    if type == 5:
        check = 'Ensemble Value'
    else:
        check = 'Predictive Label W' + str(type)
    for i in range(df.shape[0]):
        if int(df['Year'][i]) <= 2018:
            continue
        if df['True Value'][i] == "+":
            if df[check][i] == "+":
                correct[0] += 1
        else:
            if df[check][i] == "-":
                correct[1] += 1
    return correct[0], correct[1]


def false_signs(df,type):
    correct = [0, 0]
    if type == 5:
        check = 'Ensemble Value'
    else:
        check = 'Predictive Label W' + str(type)
    for i in range(df.shape[0]):
        if int(df['Year'][i]) <= 2018:
            continue
        if df['True Value'][i] == "+":
            if df[check][i] != "+":
                correct[0] += 1
        else:
            if df[check][i] != "-":
                correct[1] += 1
    return correct[0], correct[1]


def question4(df):
    for i in range(4):
        x = ["W","W","W","Ensemble"]
        true_pos, true_neg = true_signs(df, i+2)
        false_pos, false_neg = false_signs(df, i+2)
        if (true_neg+false_pos) == 0:
            true_neg_rate = 0
        else:
            true_neg_rate = true_neg/(true_neg+false_pos)
        if true_pos + false_neg == 0 :
            true_pos_rate = 0
        else:
            true_pos_rate = true_pos / (true_pos + false_neg)
        lead = x[i]+str(2+i)
        if i == 3:
            lead=x[i]
        print(lead+": \nTP: " + str(true_pos)+"\nFP: "+str(false_pos)
              +"\nTN: "+ str(true_neg) + "\nFN: " + str(false_neg) +
              "\nTPR: " + format(true_pos_rate,'.2%') + "\nTNR: " +
              format(true_neg_rate,'.2%'))


def question5(df):
    #W2 is the most accurate in both, so hard coded that for now.
    amount = [100]*3
    shares = [0,0,0]
    w_strat = []
    w_hold = False
    ensemble_strat = []
    e_hold = False
    buy_hold = []
    for i in range(df.shape[0]):
        if int(df['Year'][i]) <= 2018:
            w_strat.append(100)
            ensemble_strat.append(100)
            buy_hold.append(100)
            continue
        if shares[0] == 0:
            shares[0] = amount[0]/int(df['Open'][i])
        tmp = float(df['Close'][i])
        amount[0] = shares[0] * tmp
        buy_hold.append(amount[0])
        if df['Predictive Label W2'][i] == '+':
            if w_hold is False:
                shares[1] = amount[1]/float(df['Open'][i])
                w_hold = True
            amount[1] = shares[1] * float(df['Close'][i])
        else:
            if w_hold:
                amount[1] = shares[1]*float(df['Close'][i-1])
                shares[1] = 0
                w_hold = False
        if df['Ensemble Value'][i] == '+':
            if e_hold is False:
                shares[2] = amount[2]/float(df['Open'][i])
                e_hold = True
            amount[2] = shares[2] * float(df['Close'][i])
        else:
            if e_hold:
                amount[2] = shares[2]*float(df['Close'][i-1])
                shares[2] = 0
                e_hold = False
        w_strat.append(amount[1])
        ensemble_strat.append(amount[2])
    df["Buy & Hold Value"] = buy_hold
    df["W2 Strategy Value"] = w_strat
    df["Ensemble Strategy Value"] = ensemble_strat


def main():
    pd_dataframes = [read_file_with_true_label(ticker_files[0]),
                     read_file_with_true_label(ticker_files[1])]
    count = 0
    for df in pd_dataframes:
        if count == 0:
            count += 1
            print("SPY DATA:\n\n")
        else:
            print("\n\nDB DATA:\n\n")
        print("QUESTION 1:\n")
        question1(df)
        print("\nQUESTION 2:\n")
        question2(df)
        print("\nQUESTION 3:\n")
        question3(df)
        print("\nQUESTION 4:\n")
        question4(df)
        print("\nQUESTION 5:\n")
        question5(df)
    pd_dataframes[0].to_csv(r"G:\Documents\BUMETMSSD\Spring-2-2021\677\Assignments\SPYbuy.csv")
    pd_dataframes[1].to_csv(r"G:\Documents\BUMETMSSD\Spring-2-2021\677\Assignments\DBbuy.csv")





if __name__ == '__main__':
    main()

