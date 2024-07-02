# Question 2: The Shopping List Maker

# Task 1: Write a function that lets the user add items to a list.

shopping_list = []

def add_item(item):
    global shopping_list
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")


# Task 2: Include a function to remove items from the list.

def remove_item(item):
    global shopping_list
    shopping_list.remove(item)
    print(f"{item} has been removed from your shopping list.")


# Task 3: Add a function that prints out the entire list in a formatted way.

def display_shopping_list():
    
    if shopping_list:
        print()
        print("Shopping List: ")
        for item in shopping_list:
            print(f"- {item}")
    else:
       print("Your shopping list is empty.") 
display_shopping_list()

def user_input():
    done = False

    while not done:
        user_decision = input("Would you like to: [add] items, [remove] items, [display] shopping list, or [quit]? ").lower()

        if user_decision == "quit":
            print("Good Bye! 👋")
            display_shopping_list()
            done = True

        elif user_decision == "add":
            display_shopping_list()
            item = input("What item would you like to add to your shopping list? ").title()
            add_item(item)

        elif user_decision == "remove":
            display_shopping_list()
            item = input("What item would you like to remove from your shopping list? ").title()
            remove_item(item)

        elif user_decision == "display":
            display_shopping_list()

        else:
            print("That is not an option. Please try again.")
user_input()