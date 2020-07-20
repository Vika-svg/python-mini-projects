# 1. Let the user input the number of dice to roll.
# 2. Roll the selected amount of dice and print all values to the command line.
# 3. Remember all dice rolls by saving the outcomes in a dictionary (key/value). Keys represent dice values and values are the amount of times the given value has been thrown. Print the dictionary to the command line after each roll.

import random

class Dice:
    def __init__(self, seiten, amount_dice):
        self.seiten = seiten
        self.amount_dice = amount_dice
    
    def rollDice(self):
        randomList = []
        for i in range(0, self.amount_dice):
            randomList.append(random.randint(1, self.seiten))  
        return randomList


#num1 = Dice(int(input('Wieviel Seiten hat Deine Würfel: ')), int(input('Wieviele Würfel hast Du: ')))
#print(Dice.num(num1))

def main():
    # Game loop
    statistics = {
        1: 0, 
        2: 0, 
        3: 0, 
        4:0, 
        5:0, 
        6:0
    }
    while (True):
        print("")
        answer = input('How many dice: ')
        if (answer == "stop"):
            print("exiting")
            return

        numberOfDice = int(answer)
        dice = Dice(6, numberOfDice)
        values = dice.rollDice()
        print(values)
        
        for value in values:
            statistics[value] = statistics[value] + 1

        print(statistics)

if __name__ == "__main__":
    # execute only if run as a script
    main()