# Question 1: The Calculator App

# Task 1: Create functions for each arithmetic operation.
 
def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2
    
def multiplication(number1, number2):
    return number1 * number2
   
def division(number1, number2):
    return number1 / number2
    

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

operation_selection = input("Which operation will you be using: (+), (-), (*), (/) ")

while True:

    try:
        number1 = int(input("Please enter your first number: "))
        number2 = int(input("Please enter your second number: "))
        break
    except ValueError:
        print("Uh-oh! Please enter a whole number.")

while True:

    if operation_selection == "+":
        print(number1, "+", number2, "=", addition(number1, number2))

    elif operation_selection == "-":
        print(number1, "-", number2, "=", subtraction(number1, number2))

    elif operation_selection == "*":
        print(number1, "*", number2, "=", multiplication(number1, number2))

    elif operation_selection == "/":
        if number1 == 0 or number2 == 0:
            print("Error: You can not divide by zero. Please try again using another number.")
        else:
            print(float(number1), "/", float(number2), "=", division(float(number1), float(number2)))


# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

    elif operation_selection != "+" or "-" or "*" or "/":
        print("Invalid operation input. Please try again.")

    else:
        print("Invalid input. Please try again.")
        
    break