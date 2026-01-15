import calculator_functions
x = ""
y = ""

#For now this will be a terminal calculator. In the future we will add a GUI and more advanced features.
#at some point we will create some better way to do all this but I am still learning. Honestly I am just impressed I am using git at all
#mostly I am just using it so its easier to bounce between my desktop and laptop
def menu():
    print("""
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exponential
    6. Root
    Q --- Quit
    """)
    return

menu()
function = input("Enter a selection from the menu to select that operation\n")

#function selection section

#Addition
while function == "1":
    x = input("Enter first number to add:\nOr use type 'Q' to go back to the main menu! ")
    if x == "Q" or x == "q":
        menu()
        function = input("Enter a selection from the menu to select that operation\n")
        continue
    y = input("Enter second number to add: ")
    calculator_functions.add(x,y)


#Subtration
while function == "2":
    x = input("Enter first number to subtract:\nOr use type 'Q' to go back to the main menu! ")
    if x == "Q" or x == "q":
        menu()
        function = input("Enter a selection from the menu to select that operation\n")
        continue
    y = input("Enter second number to subtract: ")
    calculator_functions.subtract(x, y)

#multiplication
while function == "3":
    x = input("Enter first number to multiply:\nOr use type 'Q' to go back to the main menu! ")
    if x == "Q" or x == "q":
        menu()
        function = input("Enter a selection from the menu to select that operation\n")
        continue
    y = input("Enter second number to multiply: ")
    calculator_functions.multiply(x, y)

#division
while function == "4":
    x = input("Enter first number to divide:\nOr use type 'Q' to go back to the main menu! ")
    if x == "Q" or x == "q":
        menu()
        function = input("Enter a selection from the menu to select that operation\n")
        continue
    y = input("Enter second number to divide: ")
    calculator_functions.divide(x, y)

#exponent function
while function == "5":
    x = input("Enter base value:\nOr use type 'Q' to go back to the main menu! ")
    if x == "Q" or x == "q":
        menu()
        function = input("Enter a selection from the menu to select that operation\n")
        continue
    y = input("Enter exponential value\nOr use type 'Q' to go back to the main menu! ")
    calculator_functions.exponent(x, y)

#root function
while function == "6":
    x = input("Enter base value: ")
    if x == "Q" or x == "q":
        menu()
        function = input("Enter a selection from the menu to select that operation\n")
        continue
    y = input("Enter root value ")
    calculator_functions.root(x, y)