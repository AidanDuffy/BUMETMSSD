"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 15, 2020
Final Project
Description: This is the main project file for the credit card choosing program
"""

import CreditCard

def parseDatabase(database):
    """
    This takes an input file and parses through, creating a number of template
    cards
    :param database: is the opened credit card db file.
    :return: a list of template credit cards
    """
    template_wallet = list()
    line = database.readline()
    line = line[:len(line) - 1]
    holder = "template"
    while(line != "END"):
        card_parts = list(line.split(":"))
        network = card_parts[0]
        issuer = card_parts[1]
        card_name = card_parts[2]
        cash_back_points = card_parts[3]
        if "," in cash_back_points:
            cpp = float(cash_back_points[2:])
            cash_back_points = cash_back_points[0]
        else:
            cpp = 1
        sub_info = card_parts[5]
        categories = card_parts[7]
        balance = 0
        age = 0
        card = CreditCard.CreditCard(holder,network,issuer,card_name,sub_info,
                              categories,balance,age,cash_back_points, cpp)
        template_wallet.append(card)
        line = database.readline()
        line = line[:len(line) - 1]
    return template_wallet

def parseUserData(user_data):
    """
    This parses through the user's saved credit card info.
    :param user_data: is the open user cards text file
    :return: a list of all the cards the user has
    """
    template_wallet = list()
    line = user_data.readline()
    line = line[:len(line) - 1]
    while (line is not ""):
        card_parts = list(line.split(":"))
        holder = card_parts[0]
        network = card_parts[1]
        issuer = card_parts[2]
        card_name = card_parts[3]
        cash_back_points = card_parts[5]
        if "," in cash_back_points:
            cpp = float(cash_back_points[2:])
            cash_back_points = cash_back_points[0]
        else:
            cpp = 1.0
        sub_info = card_parts[6]
        sub_list = list(sub_info.split(","))
        if sub_list[0] == "False":
            sub_str = sub_info
        else:
            sub_str = sub_list[1]+","+sub_list[2]+","+sub_list[4]
        categories = card_parts[8]
        balance = card_parts[10]
        age = card_parts[9]
        card = CreditCard.CreditCard(holder, network, issuer, card_name,
                                     sub_str,
                                     categories, balance, age,
                                     cash_back_points, cpp)
        if sub_list[0] == "True":
            sub = card.getSUB()
            sub.setProgress(int(sub_list[3]))
        template_wallet.append(card)
        line = user_data.readline()
        line = line[:len(line) - 1]
    return template_wallet

def saveUserCards(wallet, user_data):
    """
    This saves all of the user card information in a text file for next time.
    :param wallet: is the list of this user's cards
    :return: none
    """
    holder = input("What is the holder's name? ")
    for card in wallet:
        network = card.getNetwork()
        issuer = card.getIssuer()
        card_name = card.getCardName()
        cash_back_points = card.checkPointsOrCash()
        cpp = card.getCPP()
        if cpp.is_integer():
            cpp = str(cpp)
            cpp = cpp[:len(cpp)-2]
        sub = card.getSUB()
        if sub.checkActive() is False:
            sub_info = "False"
        else:
            sub_info = "True,"+str(sub.getReward())+","\
                       +str(sub.getMin())+","+str(sub.getProgress())\
                       +"," + str(sub.getMonths())
        categories = card.printCategories()
        balance = card.checkBalance()
        age = card.getAge()
        line = [holder,network,issuer,card_name,cash_back_points+","+cpp,
                "SUB",sub_info,"Categories", categories,str(age),str(balance)]
        line = ":".join(line)
        user_data.write(line + "\n")

def addCard(wallet, template_wallet):
    name = input("What is your name? ")
    issuer = input("Which bank is the issuer? ")
    selected = False
    new_card = None
    for card in template_wallet:
        if card.getIssuer() != issuer:
            continue
        yesNo = ""
        while yesNo != "Y" or yesNo != "N":
            yesNo = input("Is it the " + card.getCardName()
                          + "(Input Y or N)? ")
            if yesNo == "Y":
                selected = True
                new_card = card
                break
            elif yesNo == "N":
                break
            else:
                print("Error! Please enter in Y or N!")
        if selected:
            break
    if selected is False:
        print("Error: This issuer was not found in your wallet! Try again!")
        return
    while yesNo != "Y" or yesNo != "N":
        yesNo = input("Is the card new (Input Y or N)? ")
        sub = new_card.getSUB()
        network = new_card.getNetwork()
        issuer = new_card.getIssuer()
        card_name = new_card.getCardName()
        cats = new_card.printCategories()
        cpp = new_card.getCPP()
        sub_info = str(sub.getReward())+","+str(sub.getMin())+","+\
                   str(sub.getMonths())
        if yesNo == "Y":
            balance = 0
            age = 0
            result = CreditCard.CreditCard(card_name, network,issuer,card_name,
            sub_info,cats,balance,age,new_card.checkPointsOrCash(), cpp)
            break
        elif yesNo == "N":
            while (True):
                try:
                    balance = float(input("Please enter the balance in USD: "))
                    age =int(input("Please enter the age in months of the "
                                   "card: "))
                    break
                except:
                    print("Please enter valid numbers!")

            result = CreditCard.CreditCard(card_name, network,issuer,card_name,
            sub_info, cats,balance, age, new_card.checkPointsOrCash, cpp)
            break
        else:
            print("Error! Please enter in Y or N!")

    if selected is False:
        print("It appears we do not currently support the card you are looking"
              "for! Check back again later.!")
    else:
        wallet.append(result)

def decider(wallet):
    return

def checkBalance(wallet):
    whichCard = input("Which card are you checking the balance for? (Enter"
                      "in Issuer,Card Name) ")
    card_parts = list(whichCard.split(","))
    if len(card_parts) != 2:
        print("Bad input, try again!")
        return
    else:
        for card in wallet:
            if card.getIssuer() == card_parts[0]:
                if card.getCardName() == card_parts[1]:
                    print(card.checkBalance())
                    return
        print("You either do not have this card or gave a bad input! Try"
              " again!")
        return

def makePayment(wallet):
    whichCard = input("Which card are you making a payment for? (Enter"
                      "in Issuer,Card Name) ")
    amount = input("How much are you paying off? (Use integers): ")
    try:
        amount = int(amount)
    except:
        print("Please enter a valid number next time!")
        return
    card_parts = list(whichCard.split(","))
    if len(card_parts) != 2:
        print("Bad input, try again!")
        return
    else:
        for card in wallet:
            if card.getIssuer() == card_parts[0]:
                if card.getCardName() == card_parts[1]:
                    card.payOffCard(amount)
                    return
        print("You either do not have this card or gave a bad input! Try"
              " again!")
        return

def checkSUB(wallet):
    whichCard = input("Which card are you checking the SUB for? (Enter"
                      "in Issuer,Card Name) ")
    card_parts = list(whichCard.split(","))
    if len(card_parts) != 2:
        print("Bad input, try again!")
        return
    else:
        for card in wallet:
            if card.getIssuer() == card_parts[0]:
                if card.getCardName() == card_parts[1]:
                    sub = card.getSUB()
                    res=("SUB Reward: " + sub.getReward() + "\nMinimum Spend: "
                          + sub.getMin() + "\nProgress: " + sub.getProgress()
                          + "\nMonths: " + sub.getMonths())
                    print(res)
                    return
        print("You either do not have this card or gave a bad input! Try"
              " again!")
        return
def checkCPP(wallet):
    whichCard = input("Which card are you checking the balance for? (Enter"
                      "in Issuer,Card Name) ")
    card_parts = list(whichCard.split(","))
    if len(card_parts) != 2:
        print("Bad input, try again!")
        return
    else:
        for card in wallet:
            if card.getIssuer() == card_parts[0]:
                if card.getCardName() == card_parts[1]:
                    print(card.getCPP())
        print("You either do not have this card or gave a bad input! Try"
              " again!")
        return

def main(ccdb, user_data):
    """
    This is the main method of the program
    :param ccdb: is the name of the card database text file
    :param user_data: is the name of the user card text file
    :return:
    """
    database = open(ccdb, "r+")
    user = open(user_data, "r+")

    template_wallet = parseDatabase(database)
    if len(user.read()) == 0:
        wallet_empty = True
        wallet = list()
    else:
        wallet_empty = False
        user = open(user_data, "r+")
        wallet = parseUserData(user)

    menu_value = -1
    while(menu_value != 0):
        print("Main Menu:\n\t0. Exit\n\t1. Add New Card\n\t2. Which Card Should"
              " I Use for this Purchase?\n\t3. Check Balance"
              "\n\t4. Make a Payment\n\t5. Check Sign-Up Bonus Information"
              "\n\t6. Check the Cents Per Point\n")
        menu_value = (input("Please enter one of the above values: "))
        try:
            menu_value = int(menu_value)
        except:
            print("Error: Not an integer! Please enter a valid input!")
            continue
        if menu_value == 0:
            break
        elif menu_value < 0 or menu_value > 6:
            print("Error: Not a valid integer! Please enter a valid number!")
            continue
        elif menu_value == 1:
            addCard(wallet, template_wallet)
        elif menu_value == 2:
            decider(wallet)
        elif menu_value == 3:
            checkBalance(wallet)
        elif menu_value == 4:
            makePayment(wallet)
        elif menu_value == 5:
            checkSUB(wallet)
        elif menu_value == 6:
            checkCPP(wallet)
    print("Exiting...")
    user = open(user_data, "r+")
    saveUserCards(wallet,user)
    user.close()
    database.close()



if __name__ == "__main__":
    main("Credit Card Database.txt", "user cards.txt")
