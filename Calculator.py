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
    print("Nothing Here Yet!")
    break

while function == "3":
    print("Nothing Here Yet!")
    break

while function == "4":
    print("Nothing Here Yet!")
    break

while function == "5":
    print("Nothing Here Yet!")
    break

while function == "6":
    print("Nothing Here Yet!")
    break