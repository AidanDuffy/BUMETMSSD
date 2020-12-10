"""
Class: CS521 O2, Fall, 2020
This is the skeleton file for HW6
Created 28 July 2020
The assignment was to work through inheritance by creating a list
of animals and their behaviours and putting them through their paces!
Comments in the program will explain where to insert the code using the
assignment instructions.
"""


class Pet:
    """
    This is the outermost super class for HW6, which is the most basic form of animal.
    """
    kind = "animal"
    color = "black"

    def __init__(self, name):
        """
        Constructor for Pet
        """
        self.name = name
        pass


    def __str__(self):
        """
        Returns the name, color, and kind of the given Pet in a readable format.
        """
        return self.name + " is a " + self.color + " " + self.kind + "."
        pass


    def do_tricks(self):
        """
        This notifies the user that the Pet is now doing tricks! For Dogs and Cats, it will also speak and jump.
        """
        speak = self.speak()
        jump = self.jump()
        trick = self.name + " is doing tricks!"
        if speak is not None:
            trick += "\n" + speak
        if jump is not None:
            trick += "\n" + jump
        return trick
        pass


    def speak(self):  # this will be overridden
        pass

    def jump(self):   # this will be overridden
        pass


class Jumper(Pet):
    """
    This is a mixin class for jump
    """


    def jump(self):
        """
        This notifies the user that the pet is now jumping!
        """
        return self.name + " is jumping!"
        pass


class Dog(Jumper, Pet):
    """
    Inheriting from the Pet and Jumper classes, this is a generic Dog class. The kind is canine, and
    the Owner, by default, is named Aidan.
    """
    kind = "canine"

    def __str__(self):
        """
        This returns the dog's name and color
        """
        return self.name + " is a " + self.color + " dog."
        pass


    def __call__(self):
        """
        This returns that the dog is rolling over as well as the owner's name.
        """
        return self.name + " is rolling over!\n" + self.name + "'s owner's name is Aidan."



class BigDog(Dog):
    """
    This inherits from the Dog class and simply changes the color to tan, but this is a larger dog.
    """
    color = "tan"

    def __str__(self):
        """
        This returns the large dog's name and color while describing its relative size
        """
        return self.name + " is a very large, muscular, " + self.color + " dog!"
        pass


    def speak(self):
        """
        This returns the sound a large dog makes
        """
        return self.name + " says WOOF!!!!"
        pass



class SmallDog(Dog):
    """
    This inherits from the Dog class and simply changes the color to brindle, but this is a small dog or pup.
    """
    color = "brindle"


    def __str__(self):
        """
        This returns the small dog's name and color while describing its relative size
        """
        return self.name + " is a tiny, adorable, " + self.color + " pup!"

    def speak(self):
        """
        This returns the sound a tiny dog makes
        """
        return self.name + " says Yip yip!"


class Cat(Jumper, Pet):
    """
    Inheriting from the Pet and Jumper classes, this is a generic Cat class. The kind is feline.
    """
    kind = "feline"

    def __str__(self):
        """
        This returns the name and kind of the Cat.
        """
        return self.name + " is a " + self.color + " cat."
        pass

    def speak(self):
        """
        This returns the name of the cat and the sound a cat makes.
        """
        return self.name + " says Meowww!!!!"
        pass

    def climb(self):
        """
        This informs the user that the cat with the given name is climbing on the curtains!
        """
        return self.name + " is climbing on the curtains!!!"
        pass

class HouseCat(Cat):
    """
    This inherits from the Cat class and simply changes the color to white, but this is a nonferal house cat.
    """
    color = "white"

    def __str__(self):
        """
        This returns the name along with a description of this house cat.
        """
        return self.name + " is a cat with fluffy, " + self.color + " fur."

    def speak(self):
        """
        This returns what a tamed house cat says.
        """
        return self.name + " says Purrrrr!"

def main():
    """
    Here, this program creates instances of all classes (except Jumper) then prints relevant information from
    all of them.
    :return:
    """
    petGeneric = Pet("Rover")
    cat = Cat("Caesar")
    dog = Dog("Buddy")
    bigDog = BigDog("Ajax")
    smallDog = SmallDog("Rex")
    houseCat = HouseCat("Puss-in-Boots")
    allPets = [petGeneric,cat,dog,bigDog,smallDog,houseCat]

    for pet in allPets:
        if pet.kind == "canine":
            print(pet.__str__(),pet.kind,pet.color,pet.do_tricks(), pet.__call__(),sep="\n")
        elif pet.kind == "feline":
            print(pet.__str__(),pet.kind,pet.color,pet.do_tricks(), pet.climb(),sep="\n")
        else:
            print(pet.__str__(), pet.kind, pet.color, pet.do_tricks(),sep="\n")
        print("__________________________________________")

if __name__ == "__main__":
    main()

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

