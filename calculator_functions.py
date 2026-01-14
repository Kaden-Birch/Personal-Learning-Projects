#Addition function
def add(x, y):
    answer = x + y
    print(f"{x} + {y} = {answer}")
    return

#Subtraction function
def subtract(x, y):
    answer = x - y
    print(f"{x} - {y} = {answer}")
    return


#Multiplication function
def multiply(x, y):
    answer = x * y
    print(f"{x} * {y} = {answer}")
    return

#Division function
def divide(x, y):
    while y == 0:
        print("ERROR --- CANNOT DIVIDE BY 0!")
        y = input("Enter a valid value to divide by\n")
    answer = x / y
    print(f"{x} / {y} = {answer}")
    return

#Exponent function
def exponent(x, y):
    answer = x ** y
    print(f"{x} ^ {y} = {answer}")
    return

#Root function
def root(x, y):
    math_root = 1/y
    answer = x ** math_root
    print(f"{x} ^ {y} = {answer}")
    return
