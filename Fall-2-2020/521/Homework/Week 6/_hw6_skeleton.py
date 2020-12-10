"""
Class: CS521 O2, Summer, 2020
This is the skeleton file for HW6
Created 28 July 2020
The assignment was to work through inheritance by creating a list
of animals and their behaviours and putting them through their paces!
Comments in the program will explain where to insert the code using the
assignment instructions.
"""


class Pet:
    """
    insert a class docstring
    """
    # Create two variables kind and color; assign values

    def __init__(self, name):
        """
        Constructor for Pet
        """
        # In the constructor, initialize the pets name
        pass


    def __str__(self):
        """
        insert a method docstring
        """
        # return a string with the name and description of pet so that it
        # matches the sample output from assignment
        pass


    def do_tricks(self):
        """
        insert a method docstring
        """
        # Call the speak method
        # Call the jump method
        # return the name of the pet and that it is doing tricks
        pass


    def speak(self):  # this will be overridden - leave as is
        pass

    def jump(self):   # this will be overridden - leave as is
        pass


class Jumper(Pet):
    """
    This is a mixin class for jump
    """

    def jump(self):
        """
        insert a method docstring
        """
        # return pet's name and that the Pet is jumping
        pass


class Dog():    # You will need to inherit for this to work
    """
    insert a Class docstring
    """

    # Change kind to canine


    def __str__(self):
        """
        insert the method docstring
        """

        # return the name and a description of dog so that it matches the
        # sample output from assignment
        pass


    def __call(self):
        """
        insert a method docstring
        """

        # Rollover action returns the name of the dog and that it is rolling
        # over

        # Owner action returns the name of the owner



class BigDog():    # You will need to inherit for this to work
    """
    insert a Class docstring
    """

    # Change the color to tan


    def __str__(self):
        """
        insert a method docstring
        """
        # return the name and description of BigDog so that it matches the
        # sample output from assignment
        pass


    def speak(self):
        """
        insert a method docstring
        """

        # return dogs name and what it says
        pass


class SmallDog():    # You will need to inherit for this to work
    """
    insert a Class docstring
    """

    # Change the color to brindle


    def __str__(self):
        """
        insert a method docstring
        """

        # return the name and description of SmallDog so that it matches the
        # sample output from assignment


    def speak(self):
        """
        insert a method docstring
        """
        # return dogs name and what it says

class Cat():     # You will need to inherit for this to work
    """
    insert a Class docstring
    """

    # Change the kind to feline

    def __str__(self):
        """
        insert a method docstring
        """
        # return the name and description of cat so that it matches the
        # sample output from assignment

    def speak(self):
        """
        insert a method docstring
        """
        # return cats name and what it says

    def climb(self):
        """
        insert a method docstring
        """
        # return the name of the cat and that it is climbing

class HouseCat():     # You will need to inherit for this to work
    """
    insert a Class docstring
    """
    # Change the color to white

    def __str__(self):
        """
        insert a method docstring
        """
        # return the name and description of the house cat so that it matches
        # the sample output from assignment

    def speak(self):
        """
        insert a method docstring
        """
        # return cats name and what it says


###############################################
# EXERCISES YOUR CODE
#
#    1. Instantiate each class(except Jumper)
#    2. Create a list of the instantiated objects
#    3. Loop through the objects
#    4. Print __str__
#    5. Print the Kind of pet
#    6. Print the Color of the pet
#    7. Have the pet do tricks
#    8. if applicable, print rollover action and the owners name
#    9. If applicable, have the pet climb
#   10. To separate each pet print a line of underscores
###############################################

# Your code to work with the class objects and print everything goes here!

