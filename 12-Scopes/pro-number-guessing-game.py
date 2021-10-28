import random

def set_difficulty():
    """Sets difficulty for the first time"""
    dif = input("Chose a difficult. Type easy or hard: ")
    at = set_attemps(dif)
    return dif,at

def set_attemps(dif):
    """Sets the number of attempts according with difficulty choosen"""
    if dif == "easy": return EASY_ATTEMPTS
    elif dif == "hard": return HARD_ATTEMPTS

def check_answer(number,guess):
    if guess == number:
        print("You have guessed the number! You win! Congratulations!")
        game_over = True
        return game_over
    elif guess > number:
        #print(f"->{guess}")
        print("Too high")
    elif guess < number:
        #print(f"->{guess}")
        print("Too low")
    return -1

def check_end_game(at,dif):
    """Check the guess againts the number to guess. Return the number of attempts remaining"""
    if dif == "hard":
        print("Sorry, you have not guessed the number but you have another change now, with easy difficulty")
        dif = "easy"
        at = set_attemps(dif)
        game_over = False
        return dif,at,game_over
    elif dif == "easy":
        print("You are a fucking dummy! You loose")
        game_over = True
        return dif,at,game_over


def game():
    global game_over
    from pro_guessing_logo import logo
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking in a number between 1 and 100 that you have to guess") # Generate random name and assign to CONSTANT
    NUMBER_TO_GUESS = random.randint(1,100)
    print(NUMBER_TO_GUESS)
    difficulty, attempts = set_difficulty()
    guess = 0
    
    while not game_over and guess != NUMBER_TO_GUESS:
        print(f"You have {attempts} to guess the number.")
        guess = int(input(f"Make a guess: "))
        attempts += check_answer(NUMBER_TO_GUESS,guess)
        if attempts == 0:
            difficulty,attempts,game_over = check_end_game(attempts,difficulty)

# Setting constants
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5    
game_over = False
game()
