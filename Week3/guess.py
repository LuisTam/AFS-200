secretWord = "ASTROS"
guessedLetter = []
wordBoard = ["_"]*len(secretWord)
#This makes the board show up
def showBoard():
    print(" ".join(wordBoard))
#function to check for guess starting found as a False Boolean
def checkGuess(letter):
    found = False
    #this iterates through secret word one index(i) at a time.
    for i in range(len(secretWord)):
    #this checks to see if letter at current index of secret word matches guessed letter
        if secretWord[i] == letter:
        #this matches the correct guessed letter and updates the wordboard with the right index(i)
            wordBoard[i] = letter
            found = True
    return found

#This sets the game up with secret word and shows board 
#and makes list of guessed letter as well as the number of wrong guesses
def game():
    wrongGuesses =  0
    while True:
    #Shows current board and guessed letters
        showBoard()
        print(f"Guessed letters: {' '.join(guessedLetter)}")
        #If theres no "_" on board the game is over
        if "_" not in wordBoard:
            print("Congratulations you have guessed the team!")
            break
        #this happens if user has reached the max number of tries and the game ends.
        if wrongGuesses == 5:
            print(f"Sorry game over the correct team is: {secretWord}")
            break

        guess = input("Guess a letter: ").upper()
#This checks for the lenght of the guess and ensures you only enter 1 character
#With the method .isalpha() it checks that the entered guess is a letter 
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
#This checks to see of the letter entered has already been guessed.
        if guess in guessedLetter:
            print("Letter already guessed.")
            continue
#this adds letter to guessed letter list
        guessedLetter.append(guess)
#If guess is correct: Else wrong and wrong guess counter increments by 1
        if checkGuess(guess):
            print("Correct!")
        else:
            print("Try again!")
            wrongGuesses += 1
#This calls the game function and starts the game          
print("Can you guess the baseball team?")
game()
