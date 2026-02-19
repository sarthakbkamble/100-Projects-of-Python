from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import art

coffee_menu = Menu()
nescafe_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

coffee_machine_is_on = True
print(art.coffee)
print(art.coffee_text)
while coffee_machine_is_on:
    cust_order = input(f"What would you like? ({coffee_menu.get_items()}) :").lower()
    if cust_order == "off":
        coffee_machine_is_on = False
    elif cust_order == "report":
        nescafe_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = coffee_menu.find_drink(cust_order)
        if nescafe_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            nescafe_coffee_maker.make_coffee(drink)
    