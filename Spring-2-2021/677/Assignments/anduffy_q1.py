"""
Aidan Duffy
Class: CS 677 - Spring 2
Date: 03/23/2021
Homework Problem #1
Description of Problem (just a 1-2 line summary!): This is the backend that
setups an object that tracks the sets of daily returns for a given stock.
"""
import math


class DailyReturns:

    def __init__(self, lines, year):
        self.R = dict()
        self.R_pos = dict()
        self.R_neg = dict()
        self.returns = list()
        self.opens = list()
        self.worth = 100
        prev = float(lines[1].split(",")[12]) #first close in the list
        self.shares = self.worth / prev
        self.purchased = True
        curr = 0
        gain_loss = 0
        day = ""
        for i in range (2, len(lines)):
            data = lines[i].split(",")
            if year != 0:
                if int(data[1]) < year:
                    continue
                elif int(data[1]) > year:
                    break
            curr = float(data[12])
            gain_loss = curr - prev
            day = data[4]
            if gain_loss >= 0:
                try:
                    x = len(self.R_pos[day])
                except:
                    self.R_pos[day] = list()
                self.R_pos[day].append(gain_loss)
            elif gain_loss < 0:
                try:
                    x = len(self.R_neg[day])
                except:
                    self.R_neg[day] = list()
                self.R_neg[day].append(gain_loss)
            try:
                x = len(self.R[day])
            except:
                self.R[day] = list()
            self.R[day].append(gain_loss)
            self.returns.append(gain_loss)
            self.opens.append(prev)
            prev = curr


    def mean(self, type, day):
        R_lst = dict()
        if type == 2:
            R_lst = self.R_pos
        elif type == 1:
            R_lst = self.R_neg
        else:
            R_lst = self.R
        result = 0
        days = 0
        for r in R_lst[day]:
            result += r
            days += 1
        return str(result/days)

    def stdev(self, type, day):
        R_lst = dict
        R_mean = float(self.mean(type,day))
        if type == 2:
            R_lst = self.R_pos
        elif type == 1:
            R_lst = self.R_neg
        else:
            R_lst = self.R
        result = 0
        days = 0
        for r in R_lst[day]:
            result += r**2
            days += 1
        result /= days
        result -= R_mean**2
        result = math.sqrt(result)
        return str(result)

    def oracle(self, day):
        if day == len(self.returns) - 1:
            return True
        if self.returns[day+1] > 0:
            if self.purchased is False:
                self.purchased = True
                self.shares = self.worth/(self.returns[day] + self.opens[day])
        else:
            if self.purchased:
                self.worth = self.shares*(self.returns[day] + self.opens[day])
                self.purchased = False

    def buy_and_hold(self):
        self.worth = 100
        self.shares = self.worth/self.opens[0]
        self.worth = self.shares*(self.opens[len(self.opens)-1])
        return self.worth

    def mad_oracle_a(self,day):
        sorted_vals = sorted(self.returns,reverse=True)[:10]
        if self.returns[day + 1] in sorted_vals:
            sorted_vals.remove(self.returns[day+1])
            if self.purchased:
                self.worth = self.shares * (
                            self.returns[day] + self.opens[day])
                self.purchased = False
        elif self.returns[day + 1] > 0:
            if self.purchased is False:
                self.purchased = True
                self.shares = self.worth / (
                            self.returns[day] + self.opens[day])
        else:
            if self.purchased:
                self.worth = self.shares * (
                            self.returns[day] + self.opens[day])
                self.purchased = False

    def mad_oracle_b(self,day):
        sorted_vals = sorted(self.returns)[:10]
        index = 0
        if self.returns[day + 1] in sorted_vals:
            sorted_vals.remove(self.returns[day+1])
            if self.purchased is False:
                self.purchased = True
                self.shares = self.worth / (
                        self.returns[day] + self.opens[day])
        elif self.returns[day + 1] > 0:
            if self.purchased is False:
                self.purchased = True
                self.shares = self.worth / (
                            self.returns[day] + self.opens[day])
        else:
            if self.purchased:
                self.worth = self.shares * (
                            self.returns[day] + self.opens[day])
                self.purchased = False

    def mad_oracle_c(self,day):
        sorted_vals = sorted(self.returns)
        sorted_vals = sorted_vals[0:5] + sorted_vals[-5:]
        if self.returns[day + 1] in sorted_vals[5:]:
            sorted_vals.remove(self.returns[day+1])
            if self.purchased:
                self.worth = self.shares * (
                            self.returns[day] + self.opens[day])
                self.purchased = False
        elif self.returns[day + 1] in sorted_vals[:5]:
            sorted_vals.remove(self.returns[day+1])
            if self.purchased is False:
                self.purchased = True
                self.shares = self.worth / (
                        self.returns[day] + self.opens[day])
        elif self.returns[day + 1] > 0:
            if self.purchased is False:
                self.purchased = True
                self.shares = self.worth / (
                            self.returns[day] + self.opens[day])
        else:
            if self.purchased:
                self.worth = self.shares * (
                            self.returns[day] + self.opens[day])
                self.purchased = False