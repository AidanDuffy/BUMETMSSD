# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os
import anduffy_q1

ticker = 'SPY'
input_dir = r'G:\Documents\BUMETMSSD\Spring-2-2021\677\Assignments'
ticker_file = os.path.join(input_dir, ticker + '.csv')


def print_size_avg_stdev(db_dailys):
    days = db_dailys.R.keys()
    for day in days:
        print(day + ":")
        names = ["R", "R-", "R+"]
        lists = [db_dailys.R, db_dailys.R_neg, db_dailys.R_pos]
        for i in range(3):
            print(names[i])
            print("Size: " + str(len(lists[i][day])))
            print("Average: " + db_dailys.mean(i, day))
            print("Standard Deviation:" + db_dailys.stdev(i, day))
        print()


def main():
    try:
        with open(ticker_file) as f:
            lines = f.read().splitlines()
        print('opened file for ticker: ', ticker)

        for i in range(5):
            db_dailys = anduffy_q1.DailyReturns(lines, 2016 + i)
            # print(str(2016+i) + ":")
            # print_size_avg_stdev(db_dailys)
        #    print("\n============\nAGGREGATE:\n")
        db_dailys = anduffy_q1.DailyReturns(lines, 0)
        # print_size_avg_stdev(db_dailys)
        for j in range(len(db_dailys.opens) - 1):
            db_dailys.oracle(j)
        print("Oracle returns: " + str(db_dailys.worth))
        db_dailys = anduffy_q1.DailyReturns(lines, 0)
        print("Buy and Hold value: " + str(db_dailys.buy_and_hold()))
        db_dailys = anduffy_q1.DailyReturns(lines, 0)
        for j in range(len(db_dailys.opens) - 1):
            db_dailys.mad_oracle_a(j)
        print("Mad Oracle A: " + str(db_dailys.worth))
        db_dailys = anduffy_q1.DailyReturns(lines, 0)
        for j in range(len(db_dailys.opens) - 1):
            db_dailys.mad_oracle_b(j)
        print("Mad Oracle B: " + str(db_dailys.worth))
        db_dailys = anduffy_q1.DailyReturns(lines, 0)
        for j in range(len(db_dailys.opens) - 1):
            db_dailys.mad_oracle_c(j)
        print("Mad Oracle C: " + str(db_dailys.worth))


    except Exception as e:
        print(e)
        print('failed to read stock data for ticker: ', ticker)


if __name__ == '__main__':
    main()
