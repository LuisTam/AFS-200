import random

class Die:
#this creates a die class and sets the sides to the number of sides the dice has
#also sets the current face value to None since it hasnt been rolled yet
    def __init__(self, sides):
        self.sides = sides
        self.current_face_value = None
#This dice roll generates a random(random.randint()) number between 1 and the number of the sides
#Then it updates the current_face_value to the random number generated
    def roll(self):
        self.current_face_value = random.randint(1, self.sides)
#This method gets the value currently showing on the dice  
    def getCurrentFaceValue(self):
        return self.current_face_value
#This method shows the value displaying on the dice face
    def showDieFace(self):
        print(f"{self.current_face_value}")

def yahtzee():
#This makes a list name dice and brings in the Die constructor function for each dice
#also assigns the number of sides on the die
    dice = [Die(6), Die(6), Die(6), Die(6), Die(6)]
#this loop iterates through each die in the dice list
    for die in dice:
#this calls the roll() method to each die and updates the current_face_value
        die.roll()
#This call the showDieFace() to each die and displays the current value using print(line18)
        die.showDieFace()
#This line checks that all values of the die in the dice list are equal
#using the all()function it checks that ALL the die in the list meet this condition
#it iterates and makes sure that all the dice match the first dice(dice[0])
    if all(d.getCurrentFaceValue() == dice[0].getCurrentFaceValue() for d in dice):
        print("YAHTZEE")
print("🎲🎲🎲🎲🎲")
yahtzee()