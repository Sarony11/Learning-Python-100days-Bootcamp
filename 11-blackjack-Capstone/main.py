import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
endgame = False
cont = "y"

# Define user, name, hand and score
class user:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []

def draw_user_card(user):
    card = random.choice(deck)
    user.hand.append(card)
    user.score += card

def check_hand(user):
    if (user.score == 21):
        print(f"{user.name} reached 21. {user.name} Wins!!")
        return True
    if (user.score > 21):
        endgame = True
        print(f"{user.name} passed 21. {user.name} Looses!!")
        return True
    return False
    
def wants_card(user):
        more = input(f"Do you {player.name} want another card or you want to stop? (y/n)")
        if (more == "y"): return True
        elif (more == "n"): return False
        
def show_hand(user):
    print(f"The {user.name}'s hand is: {user.hand}")

def show_score(user):
    print(f"With a score of: {user.score}")

def show_computer_1card(computer):
    print(f"The {computer.name}'s hand is: {computer.hand[0]}")

def check_hands(user,dealer):
    print(endgame)
    if(user.score == dealer.score):
        print("You both have the same, so it is draw")
    elif (user.score > dealer.score):
        print (f"You have a higer score than the dealer. {user.name} Win!")
    else:
        print (f"You have a lower score than the dealer. {dealer.name} Win!")
    return True


# Inicialize user hand
player = user("Player")
dealer = user("Dealer")

def init_player_hand(player):
    player.hand = []
    player.score = 0
    draw_user_card(player)
    draw_user_card(player)
    print(f"Your hand is: {player.hand}")

def init_computer_hand(dealer):
    dealer.hand = []
    dealer.score = 0
    draw_user_card(dealer)
    draw_user_card(dealer)
    show_computer_1card(dealer)
    


while(not endgame):
    init_player_hand(player)
    init_computer_hand(dealer)
    check_hand(player)
    while(not endgame):

        while(not endgame and wants_card(player)):
            draw_user_card(player)
            show_hand(player)
            endgame = check_hand(player)
            print(endgame)
        
        while(not endgame and (dealer.score < player.score or dealer.score < 20)):
            draw_user_card(dealer)
            show_hand(dealer)
            endgame = check_hand(dealer)
            print(endgame)

        if (not endgame):
            endgame = check_hands(player,dealer)
            print(endgame)

    endgame = input("Do you want to close the game o do you want to play again? (y/n): ")