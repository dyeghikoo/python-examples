# Hangman game
#
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if (letter in lettersGuessed) == False:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    i = 0
    lista = []
    for letter in secretWord:
        if letter in lettersGuessed:
            lista.append(letter)
        else:
            lista.append("_ ")
        i += 1
    return "".join(lista)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    string = string.ascii_lowercase
    for letter in lettersGuessed:
        string = string.replace(letter, "")
    return string

def init(secretWord):
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    print ("-----------")

def mainfunc(secretWord):
    lettersGuessed = []
    mistakesMade = 8
    while True:
        if mistakesMade == 0:
            print ("Sorry, you ran out of guesses. The word was " + secretWord)
            break
        elif isWordGuessed(secretWord, lettersGuessed):
            print ("Congratulations, you won!")
            break            
        else:
            print ("You have " + str(mistakesMade) + " guesses left")
            print ("Available Letters: " + getAvailableLetters(lettersGuessed))
            guess = input("Please guess a letter: ")
            guesslower = guess.lower()
            if guesslower in lettersGuessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            elif guesslower in secretWord:
                lettersGuessed.append(guesslower)
                print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed)) 
            else:
                lettersGuessed.append(guesslower)
                print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                mistakesMade -= 1
            print ("-----------")
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    init(secretWord)
    mainfunc(secretWord)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord = chooseWord(wordlist)
hangman(secretWord)

