#Addition function
def add(x, y):
    answer = float(x) + float(y)
    print(f"{x} + {y} = {answer}")
    return

#Subtraction function
def subtract(x, y):
    answer = float(x) - float(y)
    print(f"{x} - {y} = {answer}")
    return

#Multiplication function
def multiply(x, y):
    answer = float(x) * float(y)
    print(f"{x} * {y} = {answer}")
    return

#Division function
def divide(x, y):
    while float(y) == 0:
        print("ERROR --- CANNOT DIVIDE BY 0!")
        y = float(input("Enter a valid value to divide by\n"))
    answer = float(x) / float(y)
    print(f"{x} / {y} = {answer}")
    return

#Exponent function
def exponent(x, y):
    answer = float(x) ** float(y)
    print(f"{x} ^ {y} = {answer}")
    return

#Root function
def root(x, y):
    math_root = 1/float(y)
    answer = float(x) ** math_root
    print(f"{x} ^ {y} = {answer}")
    return
