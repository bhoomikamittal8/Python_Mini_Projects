import random

EASY_LEVEL = 10
HARD_LEVEL = 5

turns = 0
def check_answer(guess, answer, turns):
    if guess < answer:
        print("Too Low!")
        return turns-1
    elif guess > answer:
        print("Too High!!")
        return turns-1
    else:
        print(f"You guessed it Right!! The answer was {answer}")

def set_difficulty():
    level = input("Choose the level of difficulty [Easy or Hard]: ").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print("Welcome to the Number Guessing!")
    print("I'm thinking a number from 1-100")
    answer = random.randint(1,100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a Guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have runout of Guesses.GameOver! ")
        elif guess != answer:
            print("Guess again")

game()


