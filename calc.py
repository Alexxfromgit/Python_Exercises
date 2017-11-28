#Creating a file

'''
                                                        First Part of Exercise
'''

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
    if a != 0 and b != 0:
      return a / b
    else:
      return None

'''
                                                        Second Part of Exercise
'''

# Сложение, складывает любое количество чисел. Результат сумма

def addition_all(*args):
    x = 0
    for i in args:
        x += i
    return x

# Вычитание, вычитает любое количество чисел. 

def subtraction_all(*args):
    x = 0
    for i in args:
        x -= i
    return x

# Умножение любого количества чисел

def multiplication_all(*args):
    x = 0
    for i in args:
        x = x * i
    return x

