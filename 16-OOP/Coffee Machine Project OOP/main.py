from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

my_machine = CoffeeMaker()
my_menu = Menu()
my_moneyMachine = MoneyMachine()
drink = "latte"

def ask_for_coffee():
    drink = ""
    while True:
        drink = input(f"What would you like? ({my_menu.get_items()}): ")
        if drink == "report" or drink == "off":
            return drink
        elif my_menu.find_drink(drink) != None:
            return my_menu.find_drink(drink)


def power_off():
    global off
    off = True


def program():
    off = False
    while off == False:
        drink = ask_for_coffee()
        print(drink)
        if drink == "report":
            my_machine.report()
        elif drink == "off":
            power_off()
        else:
            if my_machine.is_resource_sufficient(drink) and my_moneyMachine.make_payment(drink.cost):
                my_machine.make_coffee(drink)
        

program()



""" 

    while not my_machine.is_resource_sufficient(drink):
        drink = ask_for_coffee(drink)
    if drink == "off":
        power_off()
    elif drink == "report":
        print_report()
    else:
        enter_cash(drink)
        consume_resources(drink)
        print_report()"""