# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def CheckResources(user_response, resource_dic, required_resource_dic):
    avail_water = resource_dic['water'] - required_resource_dic[user_response]['ingredients']['water']
    avail_milk = resource_dic['milk'] - required_resource_dic[user_response]['ingredients']['milk']
    avail_coffee = resource_dic['coffee'] - required_resource_dic[user_response]['ingredients']['coffee']
    if (avail_water < 0):
        shortage = "water"
    elif (avail_milk < 0):
        shortage = "milk"
    elif (avail_coffee < 0):
        shortage = "coffee"
    else:
        resource_dic['water'] = avail_water
        resource_dic['milk'] = avail_milk
        resource_dic['coffee'] = avail_coffee
        shortage = "no"
    return shortage



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
                "milk": 0,
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
    }

    to_countinue = True
    total_profit = 0
    while to_countinue:
        user_response = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_response == "off":
            to_countinue = False
        elif user_response == "report":
            print(f"Water: {resources['water']}ml \n Milk: {resources['milk']}ml \n Coffee: {resources['coffee']}g \nMoney: ${total_profit}")
        elif(user_response == 'espresso') or (user_response == 'latte') or (user_response == 'cappuccino'):
            check_res_status = CheckResources(user_response, resources, MENU)
            if check_res_status != 'no':
                print(f"Sorry there is not enough {check_res_status}.")
            else:
                print("Please insert coins.")
                quarters = float(input("how many quarters?: "))
                dimes = float(input("how many dimes?: "))
                nickel = float(input("how many nickles?: "))
                penny = float(input("how many pennies?: "))
                total_money_rec = quarters * 0.25 + dimes * 0.10 + nickel * 0.05 + penny * 0.01
                remain_balance = total_money_rec - MENU[user_response]['cost']
                if remain_balance >= 0:
                    total_profit = total_profit + MENU[user_response]['cost']
                    if remain_balance > 0:
                        print(f"Here is ${remain_balance} in change.")
                    print(f"Here is your {user_response}....Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
        else:
            print("Enter valid response.")





