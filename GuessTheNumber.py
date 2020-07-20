# Write a programme where the computer randomly generates a number between 0 and 20. The user needs to guess what the number is. If the user guesses wrong, tell them their guess is either too high, or too low. This will get you started with the random library if you haven't already used it.


import random

randomNo = random.randint(0, 20)

while True:
    guessNo = int(input('Guess a number between 0 and 20: '))
    if randomNo == guessNo:
        print("Yeah! You are right!")
        break
    elif guessNo < randomNo:
        print("The guess is too low")
    elif guessNo > randomNo:
        print ("The guess is too high")