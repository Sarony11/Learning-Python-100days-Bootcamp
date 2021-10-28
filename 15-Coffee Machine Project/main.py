""" 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.

2. Turn off the Coffee Machine by entering “off” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.

3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.

5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.

7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink."""

# MENU
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

import sys

def ask_for_coffee(flav):
    while True:
        try:
            flav = str(input("What would you like? (espresso/latte/cappuccino/report/off): "))
        except ValueError:
            print("Sorry, try again.")
            continue

        if flav.lower() not in ("espresso", "latte", "cappuccino", "report", "off"):
            print("Sorry, try again.")
        else:
            break
    return flav


def pay_for_coffe(flav):
    return flav


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffe: {resources['coffee']}g")
    print(f"Coffe: {resources['money']}€")

def resources_check(flav):
    if flav == "report" or flav == "off":
        return True
    else:
        for i in MENU[flav]["ingredients"]:
            if MENU[flav]["ingredients"][i] > resources[i]:
                print("Sorry there is not enough ingredientes. Refill or choose other drink")
                return False
        return True


def enter_cash(flav):
    e2 = int(input("Cuantas monedas de 2€: "))
    e1 = int(input("Cuantas monedas de 1€: "))
    c50 = int(input("Cuantas monedas de 50c: "))
    c20 = int(input("Cuantas monedas de 20c: "))
    c10 = int(input("Cuantas monedas de 10c: "))
    c5 = int(input("Cuantas monedas de 5c: "))
    c2 = int(input("Cuantas monedas de 2c: "))
    total = e2*2 + e1 + c50/2 + c20/5 + c10/10 + c5/20 + c2/50
    if total < MENU[flav]["cost"]:
        print("Sorry, not enough money. Money refunded")
        return False
    else:
        resources["money"] += MENU[flav]["cost"]
        change = round(total - MENU[flav]["cost"],2)
        print(f"Here is your change of {change}€")
        print(f"Here is your {flav} \U00002615 . Enjoy!")
        return True


def consume_resources(flav):
    for i in MENU[flav]["ingredients"]:
        print(i)
        resources[i] -= MENU[flav]["ingredients"][i]
    return resources


def power_off():
    sys.exit()


def program():
    flavour = {}
    while True:
        flavour = ask_for_coffee(flavour)
        while not resources_check(flavour):
            flavour = ask_for_coffee(flavour)
        if flavour == "off":
            power_off()
        elif flavour == "report":
            print_report()
        else:
            enter_cash(flavour)
            consume_resources(flavour)
            print_report()

program()
