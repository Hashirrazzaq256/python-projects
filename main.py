from dict import MENU, resources
import random
is_on = True
money = 0


def sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def coins():
    """ returns the total amount of coins inserted"""
    print("please enter coins")
    total =  int(input("how many quarters ?")) * 0.25
    total += int(input("how many dimes ?")) * 0.1
    total += int(input("how many nickles ?")) * 0.05
    total += int(input("how many pennies ?")) * 0.01
    return total


def transaction(money_paid, drink_cost):
    if money_paid >= drink_cost:
        change = round(money_paid - drink_cost,2)
        print(f"here is your {change}$")
        global money
        money = drink_cost
        return True
    else:
        print("Sorry that is not enough , money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
      resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")



while is_on:
    choice = input("what would you like espresso/latte/cappuccino ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml  ")
        print(f"Milk:{resources['milk']} ml")
        print(f"Coffee:{resources['coffee']} g")
        print(f"Money: {money}")
    else:
        drink = MENU[choice]
        if sufficient(drink["ingredients"]):
            payment = coins()
            if transaction(payment, drink['cost']):
                 make_coffee(choice, drink["ingredients"])








# coins = int(input("Please Insert coins "))
# quarters =

# pay = quarters + dimes + nickles + pennies
# if user_coffee == "espresso":

