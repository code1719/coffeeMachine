import sys

from library import MENU, resources

def subtract_resources(ingredients_needed):
    for ingredient, amount in ingredients_needed.items():
        resources[ingredient] -= amount

restart_program = True

while restart_program:
    # Prompt User What They Would Like
    user_choice = input('What would you like? (espresso, latte, cappuccino, or report): ')
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01

    if user_choice.lower() == "report":
        print("Remaining Resources:")
        for ingredient, amount in resources.items():
            print(f"{ingredient.capitalize()}: {amount}")
    elif user_choice.lower() in MENU:
        selected_drink = MENU[user_choice.lower()]
        ingredients_needed = selected_drink['ingredients']
        cost = selected_drink['cost']

        # Check if there are enough resources
        enough_resources = all(resources[ingredient] >= amount for ingredient, amount in ingredients_needed.items())

        if enough_resources:
            print(f"You chose {user_choice.capitalize()}. Please insert ${cost:.2f}.")

            # add payment logic
            while True:
                quarters = int(input("How many quarters?"))
                dimes = int(input("How many dimes?"))
                nickels = int(input("How many nickels"))
                pennies = int(input("How many pennies?"))

                total_inserted = (quarters * quarter) + (dimes * dime) + (nickels * nickel) + (pennies * penny)
                change = total_inserted - cost

                if change >= 0:
                    print(f"Your change is ${change:.2f}. Please enjoy your {user_choice}")
                    subtract_resources(ingredients_needed)
                    print("Remaining Resources:")
                    for ingredient, amount in resources.items():
                        print(f"{ingredient.capitalize()}: {amount}")
                    break
                else:
                    print("Insufficient payment. Please insert the correct amount")

            # Ask if the user wants to start a new order
            restart_program = input("Do you want to start a new order? (yes/no): ").lower() == 'yes'
        else:
            print("Sorry, there are not enough resources to make your selection.")
    elif user_choice.lower() == "off":
        print("Goodbye!")
        quit()  # Exit the program using quit()
    else:
        print("Invalid choice. Please select from espresso, latte, cappuccino, or report.")