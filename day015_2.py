# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "milk": 0,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
#     "money": 0
# }
#
# money = 0
# is_on = True
#
# input_str = input('a')
#
# if input_str == 'report':
#     get_report()
# elif input_str == 'off':
#     is_on = True
# else :
#     #measure resource if it is enough
#
#     #inset coins
#
#     #is_deal_success
#
#     #make coffee






#=======================================================================================================================







MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}

money = 0
is_on = True


def drink(drink_choose):
    """ Reture types of drink"""
    if drink_choose == "espresso" or drink_choose == "e":
        drink_choose = (MENU["espresso"])
    elif drink_choose == "latte" or drink_choose == "l":
        drink_choose = (MENU["latte"])
    elif drink_choose == "cappuccino" or drink_choose == "c":
        drink_choose = (MENU["cappuccino"])
    else:
        exit("Something is wrong!!!")
    return drink_choose

def insert_coin():
    """Return all money you put in"""
    money = 0
    money += 0.25 * (int(input("How many quarters?                               ")))
    money += 0.1 * (int(input("How many dimes?                                  ")))
    money += 0.05 * (int(input("How many nickles?                                ")))
    money += 0.01 * (int(input("How many pieces?                                 ")))
    money = round(money, 2)
    return money


def check_the_material(ingredients, resources):
    """Return Is the material is enough? True or False """
    for a in ingredients:
        if resources[a] < ingredients[a]:
            return False
    return True


def make_coffee(money):
    """Return When we finish the coffee,less the materials"""
    money -= (type_drink_choose["cost"])
    resources["water"] -= type_drink_choose["ingredients"]["water"]
    resources["milk"] -= type_drink_choose["ingredients"]["milk"]
    resources["coffee"] -= type_drink_choose["ingredients"]["coffee"]
    resources["money"] += type_drink_choose["cost"]
    print(f"Thank you!\nWish you have a good taste!\nThose are you change!  [ {round(money, 2)} ]")
    return resources


while is_on:
    input_str = input("Welcome! Which types of drink do you want?       \n  [ Espresso ] [ Latte ] [ Cappuccino ]          ").lower()
    if input_str == "report":
        print(
            f"  Water [ {resources["water"]} ]      Milk [ {resources["milk"]} ]      Coffee [ {resources["coffee"]} ]      Money [ {resources["money"]} ]")
    elif input_str == "off":
        is_on = False
        if is_on == False:
            exit()
    else :
        #~~~
        type_drink_choose = drink(input_str)
        # measure resource if it is enough——————————————————————————————————————————————————————————————————————————————————————————————————————————————
        if check_the_material(type_drink_choose["ingredients"], resources):
            print(f"You need pay [ {type_drink_choose["cost"]} ] $")
            # inset coins——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
            money = insert_coin()
            print(f"Now here are [ {money} ] $ you put in!")
            # is_deal_success———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
            if money > (type_drink_choose["cost"]):
                is_deal_success = True
            else:
                is_deal_success = False
                print("You don't have enough money!")
        else:
            is_deal_success = False
            print("Sorry,we don't have enough material...    (!!!&*_*<)")
        if is_deal_success:
            # make coffee————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
            resources = make_coffee(money)