"""
@author: naumovskiv
"""
import random
def guess(x):
    random_num=random.randint(1,x)
    guess=0
    guesses=1
    while guess!=random_num:
        guess=input(f"Guess a number between 1 and {x}: ")
        try:
            guess=int(guess)
            if guess < random_num:
                print("Sorry too low, guess again! ")
                guesses+=1
            elif guess > random_num:
                print("Sorry too high, guess again! ")
                guesses+=1
        except:
            print("That isn't a valid number")

    print(f"Correct! the number was {random_num}")
    if guesses ==1:
        print(f"Nice! You got it in just {guesses} guess!")
    else:
        print(f"It took {guesses} guesses to guess correctly.")
try:
    ranges=int(input("To which upper number would you like to guess: "))
    guess(ranges)
except:
    print("Invalid entry, exiting game.")
