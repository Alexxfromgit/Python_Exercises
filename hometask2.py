# creating file

names = ['Ann', 'Fillip', 'Monika', 'Ross', 'Sam', 'Alf', 'Roy', 'Sasha', 'Leon']

# Task1
'''Используя цикл for вывести каждый элемент списка'''

for i in range(len(names)):
    print(names[i])

# Task2
'''Используя цикл for вывести индекс каждого элемента списка'''

for i in range(len(names)):
    print(names.index(names[i]))
    
#Task3
'''Используя цикл for вывести первую букву каждого имени'''

for i in range(len(names)):
    print(names[i][0])
    
#Task3.1
'''Используя цикл for вывести последнюю букву каждого имени'''

for i in range(len(names)):
    print(names[i][-1])
    
#Task4
'''Используя цикл for вывести длину каждого имени'''

for i in range(len(names)):
    print(names[i], len(names[i]))

#Task5
'''Посчитать сумму квадратов чисел до 50'''

summ = 0

for i in range(51):
    x = i ** 2
    summ += x
    
print(summ)

#Task6
'''
Написать программу, которая возвращает Foo если число делится на 3 без остатка.
Возвращает Bar если число делится на 5 без остатка.
Возвращает FooBar если число делится и на3 и на 5 без остатка.
'''

def foo(a):
    if a % 3 == 0 and a % 5 == 0 and a != 0:
        print("FooBar")
    elif a % 3 == 0 and a % 5 != 0 and a != 0:
        print("Foo")
    elif a % 3 != 0 and a % 5 == 0 and a != 0:
        print("Bar")
    else:
        print("Something is wrong")
        
#Task7
'''
Написать программу которая находит максимальный элемент в списке
функциями min(), max() пользоваться низзя!
'''

x = [1, 33, 7, 18, 7, 9, 11, -5, 0, 12, 32]

count = x[0]

for i in range(len(x)):
    if x[i] > count:
        count = x[i]

print(count)

#Task8
'''
Написать программу которая находит минимальный элемент в списке
функциями min(), max() пользоваться низзя!
'''

x = [1, 33, 7, 18, 7, 9, 11, -5, 0, 12, 32]

count = x[0]

for i in range(len(x)):
    if x[i] < count:
        count = x[i]

print(count)

#Task9
'''
Написать программу которая сортирует список по возростанию
функциями sort() и sorted() пользоваться низзя!
'''

arr = [1, 33, 7, 18, 7, 9, 11, -5, 0, 12, 32]

x = 1

while x > 0:
    x = 0
    for k in range(len(arr) - 1):
        if arr[k+1] > arr[k]:
            s = arr[k]
            arr[k] = arr[k+1]
            arr[k+1] = s
            x += 1

print(arr)

#Task10
'''
Написать программу которая сортирует список по убыванию
функциями sort() и sorted() пользоваться низзя!
'''

arr = [1, 33, 7, 18, 7, 9, 11, -5, 0, 12, 32]

x = 1

while x > 0:
    x = 0
    for k in range(len(arr) - 1):
        if arr[k+1] < arr[k]:
            s = arr[k]
            arr[k] = arr[k+1]
            arr[k+1] = s
            x += 1

print(arr)
