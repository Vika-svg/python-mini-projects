# Make a rock-paper-scissors game where it is the player vs the computer. The computer’s answer will be randomly generated, while the program will ask the user for their input. This project will better your understanding of while loops and if statements.

from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

isPlaying = True
while isPlaying:
    user = input("Rock, Paper, Scissors - what is your input? ")

    if user == "Rock" and computer == "Scissors" or computer == "Rock" and user == "Scissors":
        print("Rock wins against scissors.")
        isPlaying = False
    elif user == "Scissors" and computer == "Paper" or user == "Paper" and computer == "Scissors":
        print("Scissors win against paper.")
    elif user == "Paper" and computer == "Rock" or user == "Rock" and computer == "Paper":
        print("Paper wins against rock.")
    else:
        print("No winner, try again.")
