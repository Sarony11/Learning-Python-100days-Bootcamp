""" # Things to do
Show logo and clean screen after each iteration
 - Show logo
 - Show score
 - Show actual caracter
 - Show vs logo
 - Show random caracter selected
 - Ask compare question
Show score
 - Show actual score
 - Show acomulative score
Show actual caracter to compare
Choose a new caracter to compare at random
 - Import random
 - Choose a number not already selected
Compare followers
 - Ask followers
 - Game over if fail
 - +1 score if sucess
Refresh the screen and start a new iteration """

import random
import os
from game_data import data
from art import logo
from art import vs


def init_game():
    score = 0
    a = random.choice(data)
    return score, a


def show_info(score, a):
    print(f"Your score is {score}")
    print(a)


def show_caractera(a):
    print(a["name"])
    print(a["description"])
    print(a["country"])
    print(a["follower_count"])


def show_caracterb(b):
    print(b["name"])
    print(b["description"])
    print(b["country"])


def ask_more_or_less(a, b, s):
    namea = a["name"]
    nameb = b["name"]
    guess = input(f"Do {namea} has MORE or LESS followers than {nameb}: ")
    if guess == "more" and a["follower_count"] >= b["follower_count"]:
        s += 1
        return s, False
    elif guess == "less" and a["follower_count"] <= b["follower_count"]:
        s += 1
        return s, False
    else:
        print("Ups... you have guessed wrong!")
        return s, True


def game(): 
    game_over = False
    score, a = init_game()
    while game_over != True:
        b = random.choice(data)
        def clear(): return os.system('cls')
        clear()
        print(logo)
        print(f"You actual score is {score}")
        show_caractera(a)
        print(vs)
        show_caracterb(b)
        score, game_over = ask_more_or_less(a, b, score)
        a = b


game()
