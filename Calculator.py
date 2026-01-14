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
while function == "1":
    x = int(input("Enter first number to add: "))
    y = int(input("Enter second number to add: "))
    calculator_functions.add(x,y)



while function == "2":
    x = int(input("Enter first number to subtract: "))
    y = int(input("Enter second number to subtract: "))
    calculator_functions.subtract(x, y)

while function == "3":
    x = int(input("Enter first number to multiply: "))
    y = int(input("Enter second number to multiply: "))
    calculator_functions.multiply(x, y)

while function == "4":
    x = int(input("Enter first number to divide: "))
    y = int(input("Enter second number to divide: "))
    calculator_functions.divide(x, y)

while function == "5":
    print("Nothing Here Yet!")
    break

while function == "6":
    print("Nothing Here Yet!")
    break