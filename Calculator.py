import calculator_functions

#For now this will be a terminal calculator. In the future we will add a GUI and more advanced features.
print("""
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exponential
6. Root
Q --- Quit
""")
function = input("Enter a selection from the menu to select that operation\n")

#function selection section

#Addition
while function == "1":
    x = int(input("Enter first number to add: "))
    y = int(input("Enter second number to add: "))
    calculator_functions.add(x,y)


#Subtration
while function == "2":
    x = int(input("Enter first number to subtract: "))
    y = int(input("Enter second number to subtract: "))
    calculator_functions.subtract(x, y)

#multiplication
while function == "3":
    x = int(input("Enter first number to multiply: "))
    y = int(input("Enter second number to multiply: "))
    calculator_functions.multiply(x, y)

#division
while function == "4":
    x = int(input("Enter first number to divide: "))
    y = int(input("Enter second number to divide: "))
    calculator_functions.divide(x, y)

#exponent function
while function == "5":
    x = int(input("Enter base value: "))
    y = int(input("Enter exponential value "))
    calculator_functions.exponent(x, y)

#root function
while function == "6":
    x = int(input("Enter base value: "))
    y = int(input("Enter root value "))
    calculator_functions.root(x, y)