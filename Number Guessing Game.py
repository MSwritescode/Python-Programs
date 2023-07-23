import random 
import time
number=random.randint(1,100) #generates a number between 1 and 100

def intro():
    print('Hey there! Welcome to the game of guesses!')
    print("May I know your name?")
    name=input()
    print(name,"I guessed a number between 1 and 100")
    time.sleep(.5)
    print("Go ahead. Guess!")

def pick():
    guessesTaken = 0
    while guessesTaken < 10: 
        time.sleep(.25)
        enter=input("Guess: ") 
        try: #check if a number was entered
            guess = int(enter) #stores the guess as an integer 

            if guess<=100 and guess>=1: #if they lie in range
                guessesTaken=guessesTaken+1 #adds one guess each time the player is wrong
                if guessesTaken<10:
                    if guess<number:
                        print("Your guess is too low")
                    if guess>number:
                        print("Your guess is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                if guess==number:
                    break #if the guess is right, then we will jump out of the while block
            if guess>100 or guess<1: #if they are not in the range
                print("That number is not in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 100")

        except: #if a number was not entered
            print("Sorry, I don't think that",enter,"is a number.")
            
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Hurray! You guessed the number in' ,guessesTaken, 'guesses!')

    if guess != number:
        print('The number I was thinking of was ' + str(number))

playagain="yes"

while playagain=="yes" or playagain=="y" or playagain=="Yes" or playagain=="Y":
    intro()
    pick()
    print("Do you want to play again?")
    playagain=input()

    while playagain=="no" or playagain=="n" or playagain=="No" or playagain=="N":
        exit()
