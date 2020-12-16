"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 15, 2020
Final Project
Description: This is the main project file for the credit card choosing program
Future Goals: Add a Wallet Class for additional accessor/mutator methods.
Add a function that prints out all a user's cards
Incorporate naming schemes to separate user info.
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
	while line != "END":
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
		card = CreditCard.CreditCard("template", network, issuer, card_name,
									 sub_info,
									 categories, balance, age,
									 cash_back_points, cpp)
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
			sub_str = sub_list[1] + "," + sub_list[2] + "," + sub_list[4]
		categories = card_parts[8]
		balance = card_parts[10]
		age = card_parts[9]
		card = CreditCard.CreditCard(holder, network, issuer, card_name,
									 sub_str,
									 categories, balance, age,
									 cash_back_points, cpp)
		if sub_list[0] == "True":
			sub = card.getSUB()
			sub.setProgress(int(card_parts[11]))
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
			cpp = cpp[:len(cpp) - 2]
		sub = card.getSUB()
		if sub.checkActive() is False:
			sub_info = "False"
		else:
			sub_info = "True," + str(sub.getReward()) + "," \
					   + str(sub.getMin()) + "," + str(sub.getProgress()) \
					   + "," + str(sub.getMonths())
		categories = card.printCategories()
		balance = card.checkBalance()
		age = card.getAge()
		line = [holder, network, issuer, card_name,
				str(cash_back_points) + "," + str(cpp),
				"SUB", sub_info, "Categories", categories, str(age),
				str(balance), str(sub.getProgress())]
		line = ":".join(line)
		user_data.write(line + "\n")


def addCard(wallet, template_wallet):
	"""
	This is adds a new card to the user wallet from the template_wallet, but
	it is populated with any user provided information, such as age of account
	and account balance.
	:param wallet: is the list of credit cards for this given user
	:param template_wallet: is list of all credit cards this program can handle
	:return: True or False depending on the success of the function.
	"""
	name = input("What is the name on the card? ")
	issuer = input("Which bank is the issuer? ")
	selected = False
	new_card = None
	yesNo = ""
	for card in template_wallet:
		if card.getIssuer() != issuer:
			continue
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
		p_or_c = new_card.checkPointsOrCash()
		cpp = new_card.getCPP()
		sub_info = str(sub.getReward()) + "," + str(sub.getMin()) + "," + \
				   str(sub.getMonths())
		if yesNo == "Y":
			balance = 0
			age = 0
			result = CreditCard.CreditCard(name,network, issuer,card_name,
										   sub_info, cats, balance, age,
										   p_or_c, cpp)
			break
		elif yesNo == "N":
			while (True):
				try:
					balance = float(input("Please enter the balance in USD: "))
					age = int(input("Please enter the age in months of the "
									"card: "))
					break
				except:
					print("Please enter valid numbers!")

			result = CreditCard.CreditCard(name, network, issuer, card_name,
										   sub_info, cats, balance, age,
										   p_or_c, cpp)
			break
		else:
			print("Error! Please enter in Y or N!")

	if selected:
		wallet.append(result)
	return selected


def decider(wallet):
	"""
	This checks the best card to use for a given purchase.
	:param wallet: is the list of credit cards for this given user
	:return: True or False depending on the success of the function.
			 if True, it will return a list:the card issuer, name,
			 the spending category and the value of the rewards.
	Future Goals: Update to include a map to consolidate the menu section,
	ex: {"Food":"dining,groceries"}; find out how to not have to hardcode
	quarterly categories for card like the Chase Freedom Flex/Discover It.
	Add larger functionality generally for deciding on subcategories.
	Add Wallet object, which will have flags for the best travel card or best
	dining card.
	"""
	found = False
	if len(wallet) == 0:
		return found
	elif len(wallet) == 1:
		card = wallet[0]
		found = list()
		found.append(card.getIssuer())
		found.append(card.getCardName())
		found.append(-1)
		return found
	"""
	First, we need to check for any valid SUBs. If so, if there is one,
	then that will be selected, otherwise, narrow the options to just 
	those with active SUBs and do the usual process.
	"""
	sub_cards = list()
	subs = False
	for card in wallet:
		sub = card.getSUB()
		if sub.checkActive():
			sub_cards.append(card)
	if len(sub_cards) == 1:
		found = list()
		card = sub_cards[0]
		found.append(card.getIssuer())
		found.append(card.getCardName())
		found.append(0)
	elif len(sub_cards) > 1:
		subs = True
	menu_value = -1
	while (menu_value < 0 or menu_value > 6):
		print("Spending Categories:\n\t1. Food\n\t2. Travel\n\t3. Transit"
			  "\n\t4. Gas\n\t5. Online Shopping\n\t6. Other\n")
		menu_value = input("Please enter one of the above values or 0 "
						   "to cancel: ")
		try:
			menu_value = int(menu_value)
		except:
			print("Error: Not an integer! Please enter a valid input!")
			continue
		category = ""
		if menu_value == 0:
			break
		elif menu_value < 0 or menu_value > 6:
			print("Error: Not a valid integer! Please enter a valid number!")
			continue
		elif menu_value == 1:
			print("You have selected Food! Please select a subcategory:\n\t"
				"1. Dining\n\t2. Groceries")
			subcategory = input("Please enter an above values, anything else "
					"to leave this category: ")
			try:
				subcategory = int(subcategory)
				if subcategory == 1:
					category = "dining"
				elif subcategory == 2:
					amazon = ""
					while amazon != "N" and amazon != "Y":
						amazon = input(
							"Are you shopping at Whole Foods? (Y/N):  ")
						if amazon == "N":
							category = "grocery"
						elif amazon == "Y":
							category = "grocery(Whole Foods)"
						else:
							print("Invalid input")
				else:
					print("Exiting the food category...")
					continue
			except:
				print("Exiting the food category...")
				continue
		elif menu_value == 2:
			print("You have selected Travel! Please select a subcategory:\n"
				"\t1. Flights\n\t2. Hotels\n\t3. Chase\n\t4. AMEX")
			subcategory = input("Please enter an above value, anything else to "
					"leave this category: ")
			try:
				subcategory = int(subcategory)
				if subcategory == 1:
					category = "travel"
				elif subcategory == 2:
					print("You have selected Hotel! Are you booking:\n\t1."
						  "With an IHG partner\n\t2. Elsewhere")
					subcategory = int(input("Option: "))
					if subcategory == 1:
						category = "hotel(IHG)"
					else:
						category = "travel"
				elif subcategory == 3:
					category = "travel(Chase)"
				elif subcategory == 4:
					category = "travel(AMEX)"
				else:
					print("Exiting the Travel category...")
					continue
			except:
				print("Error! Exiting the Travel category...")
				continue
		elif menu_value == 3:
			category = "transit"
		elif menu_value == 4:
			category = "gas"
		elif menu_value == 5:
			print("You have selected Online Shopping! Please select a "
				  "subcategory:\n\t1. Amazon\n\t2. Walmart\n\t3. Elsewhere")
			subcategory = input(
				"Please enter an above value, anything else to "
				"leave this category: ")
			try:
				subcategory = int(subcategory)
				if subcategory == 1:
					category = "online shopping(Amazon)"
				elif subcategory == 2:
					category = "online shopping(Walmart)"
				elif subcategory == 3:
					category = "online shopping"
				else:
					print("Exiting the Online Shopping category...")
					continue
			except:
				print("Error! Exiting the Online Shopping category...")
				continue
		elif menu_value == 6:
			print("You have selected Other! Please select a subcategory:\n\t1."
					" Streaming\n\t2. Utilies\n\t3. Drugstores\n\t4. Other")
			subcategory = input("Please enter an above value, anything else to "
					"leave this category: ")
			try:
				subcategory = int(subcategory)
				if subcategory == 1:
					category = "streaming"
				elif subcategory == 2:
					category = "utilities"
				elif subcategory == 3:
					category = "drugstores"
				elif subcategory == 4:
					category = "else"
				else:
					print("Exiting the Other category...")
					continue
			except:
				print("Error! Exiting the Other category...")
				continue
		paypal = ""
		while paypal != "N" and paypal != "Y":
			paypal = input(
				"Will you be purchasing through PayPal? (Y/N):  ")
			if paypal == "Y":
				category = category + "(PayPal)"
				break
			elif paypal == "N":
				break
			else:
				print("Invalid input")
		break
	best = list()
	best.append(0)
	best.append(0)
	tie = list()
	if subs:
		for card in sub_cards:
			sub = card.getSUB()
			value = card.checkCategory(category)
			if "(" in category:
				if "PayPal" in category:
					category = category[:len(category) - 8]
					if (card.checkCategory("quarterly") !=
							card.checkCategory("else")):
						value = card.checkCategory("quarterly")
						value += card.checkCategory(category)
				if "IHG" in category:
					if value != 25 * .6:
						value += card.checkCategory("travel")
				if "Whole Foods" in category:
					if value == card.checkCategory("else"):
						value += card.checkCategory("grocery")
				if "Amazon" in category:
					if value == card.checkCategory("else"):
						value += card.checkCategory(
							"online shopping")
			value += sub.getROS()
			if value > best[0]:
				best[0] = value
				best[1] = card
				tie = list()
			elif value == best[0]:
				tie.append(card)
				tie.append(best[1])
			value = 0
		print("Note: This recommendation is made because"
			  " of a sign-up bonus, not only multipliers!")
	else:
		for card in wallet:
			value = card.checkCategory(category)
			if "(" in category:
				if "PayPal" in category:
					temp = category[:len(category) - 8]
					if card.checkCategory(
							"quarterly") != card.checkCategory(
						"else"):
						value = card.checkCategory("quarterly")
						value += card.checkCategory(temp)
				if "IHG" in category:
					if value != 25 * .6:
						value += card.checkCategory("travel")
				if "Whole Foods" in category:
					if value == card.checkCategory("else"):
						value += card.checkCategory("grocery")
				if "Amazon" in category:
					if value == card.checkCategory("else"):
						value += card.checkCategory(
							"online shopping")
			if value > best[0]:
				best[0] = value
				best[1] = card
				tie = list()
			elif value == best[0]:
				if len(tie) == 0:
					tie.append(best[1])
				tie.append(card)
			value = 0
	found = list()
	if len(tie) == 0:
		card = best[1]
		found.append(card.getIssuer())
		found.append(card.getCardName())
		found.append(category)
		found.append(best[0])
	else:
		found.append("tie")
		found.append(tie)
		found.append(category)
		found.append(best[0])
	return found


def checkBalance(wallet):
	"""
	This checks the balance on a given user card.
	:param wallet: is the list of credit cards for this given user
	:return: True or False depending on the success of the function.
			 if True, it will return a list:the card issuer, name, and balance.
	"""
	whichCard = input("Which card are you checking the balance for? (Enter "
					  "in Issuer,Card Name) ")
	card_parts = list(whichCard.split(","))
	found = False
	if len(card_parts) == 2:
		for card in wallet:
			if card.getIssuer() == card_parts[0]:
				if card.getCardName() == card_parts[1]:
					found = card_parts
					found.append(card.checkBalance())
					break
	return found


def makePayment(wallet):
	"""
	This makes a payment to a given user card.
	:param wallet: is the list of credit cards for this given user
	:return: True or False depending on the success of the function.
			 if True, it will return a list:the card issuer and name.
	"""
	whichCard = input("Which card are you making a payment for? (Enter "
					  "in Issuer,Card Name) ")
	amount = input("How much are you paying off? (Use integers): ")
	found = False
	try:
		amount = int(amount)
	except:
		return found
	card_parts = list(whichCard.split(","))
	if len(card_parts) == 2:
		for card in wallet:
			if card.getIssuer() == card_parts[0]:
				if card.getCardName() == card_parts[1]:
					card.payOffCard(amount)
					found = card_parts
					found.append(amount)
					break
	return found


def checkSUB(wallet):
	"""
	This checks the sign up bonus information of a given user card.
	:param wallet: is the list of credit cards for this given user
	:return: True or False depending on the success of the function.
			 if True, it will return a list: sign-up bonus object and
			 the card issuer and name.
	"""
	whichCard = input("Which card are you checking the SUB for? (Enter "
					  "in Issuer,Card Name) ")
	card_parts = list(whichCard.split(","))
	found = False
	if len(card_parts) == 2:
		for card in wallet:
			if card.getIssuer() == card_parts[0]:
				if card.getCardName() == card_parts[1]:
					found = list()
					found.append(card.getSUB())
					found.append(card.getIssuer())
					found.append(card.getCardName())
					break
	return found


def checkCPP(wallet):
	"""
	This checks the cents per point value of a given user card.
	:param wallet: is the list of credit cards for this given user
	:return: True or False depending on the success of the function.
			 if True, it will return a list: the issuer, name, and CPP
	"""
	whichCard = input("Which card are you checking the balance for? (Enter "
					  "in Issuer,Card Name) ")
	card_parts = list(whichCard.split(","))
	found = False
	if len(card_parts) == 2:
		for card in wallet:
			if card.getIssuer() == card_parts[0]:
				if card.getCardName() == card_parts[1]:
					found = card_parts
					found.append(card.getCPP)
					break
	return found


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
	while (menu_value != 0):
		print(
			"Main Menu:\n\t0. Exit\n\t1. Add New Card\n\t2. Which Card Should"
			" I Use for this Purchase?\n\t3. Check Balance"
			"\n\t4. Make a Payment\n\t5. Check Sign-Up Bonus Information"
			"\n\t6. Check the Cents Per Point\n")
		menu_value = (input("Please enter one of the above values: "))
		try:
			menu_value = int(menu_value)
		except:
			print("Error: Not an integer! Please enter a valid input!")
			continue
		print("\n\n")
		function_success = False
		if menu_value == 0:
			break
		elif menu_value < 0 or menu_value > 6:
			print("Error: Not a valid integer! Please enter a valid number!")
			continue
		elif menu_value == 1:
			function_success = addCard(wallet, template_wallet)
			if function_success:
				print("Successfully added your card to your digital wallet!")
			else:
				print("It appears we do not currently support the card you are"
					  "looking for! Check back again later.!")
			continue
		elif menu_value == 2:
			function_success = decider(wallet)
			if function_success:
				reward = function_success[3]
				category = function_success[2]
				if function_success[0] == "tie":
					print("It's a tie for purchases in the", category,
						  "category. You should see a", reward,"percent"
						  " return with the following cards:")
					for card in function_success[1]:
						print("\t",card.getIssuer(),card.getCardName())
				card_name = function_success[1]
				card_issuer = function_success[0]
				if category == -1:
					print("Success! You only have one card: the", card_issuer,
						  card_name, "is what you use for all purchases!")
				elif category == 0:
					print("Success! You have one card with an active SUB: use",
						  "the", card_issuer, card_name, "for all purchases!")
				else:
					print("Success! Use the", card_issuer, card_name, "for",
						  "purchases in the", category, "category. You "
						  "should see a", reward,"percent return!")
		elif menu_value == 3:
			function_success = checkBalance(wallet)
			if function_success:
				balance = function_success[0]
				card_name = function_success[2]
				card_issuer = function_success[1]
				print("Success! The balance on your", card_issuer,
					  card_name, "is", balance, ".")
		elif menu_value == 4:
			function_success = makePayment(wallet)
			if function_success:
				card_name = function_success[1]
				card_issuer = function_success[0]
				payment = function_success[2]
				print("Success! You have made a payment on your",
					  card_issuer, card_name, "of", payment, "!")
		elif menu_value == 5:
			function_success = checkSUB(wallet)
			if function_success:
				sub = function_success[0]
				card_name = function_success[2]
				card_issuer = function_success[1]
				if sub.checkActive() is False:
					print("Success! Unfortunately, your ", card_issuer, " ",
						  card_name, "'s sign-up bonus is no longer active",
						  sep="")
					continue
				print("Success! Here is the sign-up bonus information for" \
					 " your",card_issuer,card_name, ":\n\tSUB " \
					 "Reward:", str(sub.getReward()),\
					 "\n\tMinimum Spend:",\
					 str(sub.getMin()),"\n\tProgress: ",\
					 str(sub.getProgress()),"\n\tMonths: ",\
					 str(sub.getMonths()),"\n\n")
		elif menu_value == 6:
			function_success = checkCPP(wallet)
			if function_success:
				print("Success! The", function_success[0], function_success[1],
					  "point value in cents per point (CPP) is",
					  function_success[2])
			if function_success is False:
				print(
					"Failure... You either do not have this card or gave a bad"
					"input! Try again!")
	print("Exiting...")
	user = open(user_data, "r+")
	saveUserCards(wallet, user)
	user.close()
	database.close()


if __name__ == "__main__":
	main("Credit Card Database.txt", "user cards.txt")
