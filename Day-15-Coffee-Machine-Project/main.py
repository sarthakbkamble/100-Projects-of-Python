import art

# Global configuration: Menu contains ingredients and prices for each drink
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

# Machine state: Current stock of ingredients
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Tracking total earnings
profit = {"money": 0}

def check_resources(order):
    """
    Checks if the machine has enough ingredients to fulfill the selected order.
    Returns False and prints a warning if any ingredient is insufficient.
    """
    for item in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def check_amount(order):
    """
    Handles the payment process. Calculates total from coins inserted, 
    verifies if it covers the cost, and handles change/refunds.
    Returns True if transaction is successful, False otherwise.
    """
    cost_of_order = MENU[order]["cost"]
    print(f"You have to pay ${cost_of_order} for the {order}")
    
    # Gathering user input for coins
    penny = int(input("Number of pennies inserted:"))
    nickel = int(input("Number of nickels inserted:"))
    dime = int(input("Number of dimes inserted:"))
    quarter = int(input("Number of quarter inserted:"))

    # Coin math: converting counts to dollar values
    total_amount_received = (penny * 0.01) + (nickel * 0.05) + (dime * 0.10) + (quarter * 0.25)
    
    if cost_of_order > total_amount_received:
        print(f"Sorry that's not enough money. Money refunded: ${round(total_amount_received, 2)}.")
        return False
    else:
        # Successful payment logic: add to profit and calculate change
        change = round(total_amount_received - cost_of_order, 2)
        if change > 0:
            print(f"Here is your change: ${change}")
        profit["money"] += cost_of_order
        return True

# --- Main Program Execution ---
coffee_machine_is_on = True
print(art.coffee)
print(art.coffee_text)

while coffee_machine_is_on:
    cust_order = input("What would you like? (espresso/latte/cappuccino):").lower()

    # Secret commands for the maintainer
    if cust_order == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
    elif cust_order == "off":
        print("Coffee machine turned off.")
        coffee_machine_is_on = False
    elif cust_order == "balance":
        print(f"Money in Coffee Machine: ${profit['money']}")
        
    # Standard customer flow
    elif cust_order in MENU:
        # Step 1: Resource check
        if not check_resources(cust_order):
            print("Come back after some time.")
        # Step 2: Payment check
        elif check_amount(cust_order):
            # Step 3: Deplete resources and serve drink
            for item in MENU[cust_order]["ingredients"]:
                resources[item] -= MENU[cust_order]["ingredients"][item]
            print(art.coffee)
            print(f"Here is your {cust_order.capitalize()}. Enjoy!!")
            print("\n")
        else: 
            print("Invalid input.")