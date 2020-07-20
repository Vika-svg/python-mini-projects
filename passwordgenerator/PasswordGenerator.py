# Write a programme, which generates a random password for the user. Ask the user how long they want their password to be, and how many letters and numbers they want in their password. Have a mix of upper and lowercase letters, as well as numbers and symbols. The password should be a minimum of 6 characters long.

import random
import string

# get info from user
i = True
while i:
    passwordLength = int(input('How long should the password be? '))
    # check password lenght
    if passwordLength >= 6:
        i = False
    else:
        print('Password should be a minimum of 6 characters long')
        
letterCount = int(input('How many letters should be in the password? '))
numberCount = int(input('How many numbers should be in the password? '))
punctuationCount = passwordLength - letterCount - numberCount

# generat random letter list
def randomLetters(count):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(count))

# generat random number list
def randomNumbers(count):
    numbers = string.digits
    return ''.join(random.choice(numbers) for i in range(count))

# generat random list of punctuation
def randompunctuation(count):
    punctuations = string.punctuation
    return ''.join(random.choice(punctuations) for i in range(count))

# generat Password
def password_generator(length):
    printable = f'{randomLetters(letterCount)}{randomNumbers(numberCount)}{randompunctuation(punctuationCount)}'
    return printable

print(password_generator(passwordLength))