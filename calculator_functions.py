#add function
def add(x, y):
    answer = x + y
    print(f"{x} + {y} = {answer}")
    return

def subtract(x, y):
    answer = x - y
    print(f"{x} - {y} = {answer}")
    return

def multiply(x, y):
    answer = x * y
    print(f"{x} * {y} = {answer}")
    return

def divide(x, y):
    answer = x / y
    print(f"{x} / {y} = {answer}")
    return

def exponent(x, y):
    answer = x ** y
    print(f"{x} ^ {y} = {answer}")
    return

def root(x, y):
    math_root = 1/y
    answer = x ** math_root
    print(f"{x} ^ {y} = {answer}")
    return
