import random
import sys


# lets set some variables
wordList = [
"deadpool", "avenger", "hulk", "spider", "shield", "fury", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cable", "mirror", "hat"
           ]

guess_word = []
secretWord = random.choice(wordList) # lets randomize single word from the list
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []
playername = []


def beginning():
    print("Hello!\n")

    while True:
        playername = input("It's nice to meet you. What's your name?\n").strip()

        if playername == '':
            print("You can't do that! No blank lines")
        else:
            break
    print(playername)

beginning()



def newFunc():
    print("Okay ", playername, ", would you like to play Hangman?\n")

    while True:
        gameChoice = input("Would You? Enter Y/N\n").upper()

        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("Please Answer only Yes or No")
            continue

newFunc()



def change():

    for character in secretWord: # printing blanks for each letter in secret word
        guess_word.append("-")

    print("Ok, so the word You need to guess has", length_word, "characters")

    print("Be aware that You can enter only 1 letter from a-z\n\n")

    print(guess_word)



def guessing():
    guess_taken = 1

    while guess_taken < 10:


        guess = input("Pick a letter\n").lower()

        if not guess in alphabet: #checking input
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage: #checking if letter has been already used
            print("You have already guessed that letter!")
        else: 

            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for x in range(0, length_word): #This Part I just don't get it
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                    print("Sorry", playername, ", You lost! The secret word was",         secretWord)


change()
guessing()

print("Game Over!")
