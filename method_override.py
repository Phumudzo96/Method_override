name = input("Enter your name: ")
age = int(input("Enter your age: "))                   # ask user to enter a couple of inputs
hair_colour = input("Enter your hair colour: ")
eye_colour = input("Enter your eye colour: ")

class Adult():                                          # create a class called "Adult"
    
    name = name                                         # create varibles with inputs as values
    age = age
    hair_colour = hair_colour
    eye_colour = eye_colour

    def can_drive(self):                                # create a mention called "can_drive"
        print(self.name)
        print("Old enough to drive")

class Child(Adult):                                    # Create a subclass of the adult class

    def can_drive(self):
        print(self.name)
        print("Too young to can drive")

if age >= 18:                                          # created logic based on the users inputs
    adult1 = Adult()

    adult1.can_drive()
else:
    child1 = Child()

    child1.can_drive()