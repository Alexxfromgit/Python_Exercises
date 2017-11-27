#Creating a file

#Summ function

def summ(a, b):
    return a + b

#Subtraction function

def sub(a, b):
    return a - b

#Multiplication function

def mul(a, b):
    return a * b

#Division function

def div(a, b):
    return a / b

#Addition_all

def addition_all(*args):
    x = 0
    for i in args:
        x += i
    return x

#Subtraction_all

def subtraction_all(*args):
    x = 0
    for i in args:
        x -= i
    return x


