# This is probably the hardest one out of these 6 small projects. This will be similar to guessing the number, except we are guessing the word. The user needs to guess letters. Give the user no more than 6 attempts for guessing wrong letter. This will mean you will have to have a counter. You can download a ‘sowpods’ dictionary file or csv file to use as a way to get a random word to use.

import random

# 1. Programm picks a word
# Using readlines() 
file1 = open('hangman/sowpods.txt', 'r') 
words = list(file1)

random_word = random.choice(words).strip()

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def game (random_word):
    turn = 0
    guessed_letters = '_' * len(random_word)

    while turn  < 6:
        letter = input('What is your guess: ')

        if letter.upper() == random_word:
            print('Wow, Good work!')
            break 

        if letter.upper() in random_word:
            occurrences = find(random_word, letter.upper())
            for index in occurrences:
                guessed_letters = guessed_letters[:index] + letter + guessed_letters[index + 1:]
        else:
            print('Incorrect. Try again!')
            turn += 1
            
        # results until now
        print(guessed_letters)

        if guessed_letters.upper() == random_word:
            print('Good work')
            break

# Guessing the letters
if __name__ == '__main__':
    wordLength = len(random_word)
    looking_for = '_ ' * wordLength
    print(looking_for, "(" + str(wordLength) + ")")
    game(random_word)

