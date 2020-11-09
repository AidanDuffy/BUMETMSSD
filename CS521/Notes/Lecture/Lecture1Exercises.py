
def main():
	side = input("What is the size of on side of the cube? ")
	side = float(side)
	volume = side**3
	print("The volume of the cube is ", volume)

	inp = input("Give an input to repeated thrice: ")
	#print(inp*3)
	for i in range(3):
		print(inp)

	farenheit = input("What is the temperature in degrees Farenheit? ")
	farenheit = float(farenheit)
	celsius = (5/9)*(farenheit-32)
	print("It is ", celsius, " degrees Celsius")