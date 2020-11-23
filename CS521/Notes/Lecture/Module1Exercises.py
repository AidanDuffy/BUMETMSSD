side = input("What is the size of on side of the cube? ")
side = float(side)
volume = side ** 3
print("The volume of the cube is ", volume)

inp = input("Give an input to repeated thrice: ")
# print(inp*3)
for i in range(3):
    print(inp)

farenheit = input("What is the temperature in degrees Farenheit? ")
farenheit = float(farenheit)
celsius = (5 / 9) * (farenheit - 32)
print("It is ", celsius, " degrees Celsius")


def print_1(x):
    print(x)


x = 'morning '
print_1(x)  # morning


def print_2(x):
    x = 'evening '
    print(x)


x = 'morning '
print_2(x)  # evening

x = 0
y = 0
z = 10
if z > 25:
    x = z ** 2
    y = z ** 3
print(x, y)  # 0 0

x = 0
y = 0
z = 10
if z > 25:
    x = z ** 2
y = z ** 3
print(x, y)  # 0, 1000
