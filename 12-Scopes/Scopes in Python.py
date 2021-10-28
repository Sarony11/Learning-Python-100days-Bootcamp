############ SCOPES #############

enemies = 1

def increase_enemies ():
    enemies = 2
    print(f"My local number of enemies is {enemies}")

increase_enemies()
print(f"My global number of enemies is {enemies}")

### LOCAL SCOPE ####

def drink_potion():
    potion_str = 2
    print(potion_str)

drink_potion()
print(potion_str) # This will give error because is calling to a local variable

### GLOBAL SCOPE ###
player_health = 10

def drink_potion():
    potion_str = 2
    print(player_health) # This will print the player_health global variable


def game():
    def drkin2


### In Python there is no global block scope ###
# In python, when creating variables inside a block, this variable is considered global and is not limited to the block.

game_level = 3
def create_enemy():
    enemies = ["Skeleton","Zombie"."Alien"]
    if game_level < 5:
        new_enemy = enemiges[0]

print(new_enemy)