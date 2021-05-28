import random

Hangman_parts = ['''
  +---+
      |
      |
      |
    ===''', '''
  +---+
  O   |
      |
      |
    ===''', '''
  +---+
  O   |
  |   |
      |
    ===''', '''
  +---+
  O   |
 /|   |
      |
    ===''', '''
  +---+
  O   |
 /|\  |
      |
   ===''', '''
  +---+
  O   |
 /|\  |
 /    |
    ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
    ===''']

# words = input("Please enter the word you wish to play: ").lower()
# counter = 0
# for i in words:
#     counter += 1
# print("You are expected to guess a/an " + str(counter) + " - character secret word")


inputWord = input("Please enter the word you wish to play: ").lower()
words = [inputWord] # save to a list

print(chr(27) + "[2J") # clear the screen

# returns a random string from the word or phrase.
def getRandomWord(wordsList):
    wIndex = random.randint(0, len(wordsList) - 1)
    return wordsList[wIndex]

# display the hangman board
def display_body_part(missedLetters, correctLetters, secretWord):
    print(Hangman_parts[len(missedLetters)])
    print()

    print('Missed letters:', end = ' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()

    # Displaying the Secret word with Blanks
    blanks = '_' * len(secretWord)

    # Replace the blanks with the letters guessed correctly
    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    # the secret word with spaces in between each letter.
    for letter in blanks:
        print(letter, end = ' ')
    print()

# Retrieve the single letter the player entered
def getWord(chWord):

    while True:
        print("Guess a letter to save the hangman!")
        guWord = input()
        guWord = guWord.lower()

        if len(guWord) != 1:
            print("Please do enter a word or a phrase...")
        elif guWord not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a Letter!")
        elif guWord in chWord:
            print("You have choosen the letter already, choose again...")
        else:
            return guWord

# Returns true if the player wants to continue
def repeatGame():

    try:    
        print("Do you wish to continue? (yes or no)")
        return input().lower().startswith("y")
    except Exception as err:
        print("Wrong Input: Input to play again")
        print(str(err))

print("Let the HANGMAN Game Begin")
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameCompleted = False


while True:
    display_body_part(missedLetters, correctLetters, secretWord)

    # the player should enter a letter
    guWord = getWord(missedLetters + correctLetters)

    if guWord in secretWord:
        correctLetters = correctLetters + guWord

        # winning!
        AllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                AllLetters = False
                break
        if AllLetters:
            print("CORRECT! You got the secret characters word: " + secretWord + ". - You have WON the Game!!!")

            gameCompleted = True
            break
            
    else:
        missedLetters = missedLetters + guWord
        # losing!
        if len(missedLetters) == len(Hangman_parts) - 1:
            display_body_part(missedLetters, correctLetters, secretWord)
            print("You have no moves left, so You LOSE!!! After " + str(len(missedLetters)) + " guesses and " + str(len(correctLetters)) + " correct guesses, the word is: " + secretWord.upper())

            gameCompleted = True
            break
     

