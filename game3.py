# importing the time module
import time
import sys

# welcoming the user
name = input("What is your name? ")

print
"Hello, " + name, "Time to play hangman!"

print
""

# wait for 1 second
time.sleep(1)

print
"Start guessing..."
time.sleep(0.5)

# generates random word
import random

# Establish a list of words that can be chosen for the game
with open("words.txt") as f:
    wordList = f.read().splitlines()
word = random.choice(wordList)
# creates an variable with an empty value
guesses = ''
length_word = len(word)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []
playername = []

# determine the number of turns
turns = 10

# Create a while loop

# check if the turns are more than zero
while turns > 0:

    # make a counter that starts with zero
    failed = 0

    # for every character in secret_word
    for char in word:

        # see if the character is in the players guess
        if char in guesses:

            # print then out the character
            print
            char,

        else:

            # if not found, print a dash
            print
            "_",

            # and increase the failed counter with one
            failed += 1

            # if failed is equal to zero

    # print You Won
    if failed == 0:
        print
        "You won"

        # exit the script
        break

    print

    # ask the user to guess a character
    guess = input("guess a character:")

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:

        # turns counter decreases with 1 (now 9)
        turns -= 1

        # print wrong
        print
        "Wrong"

        # how many turns are left
        print
        "You have", + turns, 'more guesses'

        # if the turns are equal to zero
        if turns == 0:
            # print "You Lost"
            print
            "You Lost, sad face"
            print
            "the word was:"
            print(word)