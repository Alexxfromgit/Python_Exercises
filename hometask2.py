# creating file


names = ['Ann', 'Fillip', 'Monika', 'Ross', 'Sam', 'Alf', 'Roy', 'Sasha', 'Leon']

# Task1
for i in range(len(names)):
    print(names[i])

# Task2
for i in range(len(names)):
    print(names.index(names[i]))
    
#Task3
for i in range(len(names)):
    print(names[i][0])
    
#Task4
for i in range(len(names)):
    print(names[i], len(names[i]))

#Task5
summ = 0

for i un range(51):
    x = i ** 2
    summ += x
    
print(summ)

#Task6
def foo(a):
    if a % 3 == 0 and a % 5 == 0 and a != 0:
        print("FooBar")
    elif a % 3 == 0 and a % 5 != 0 and a != 0:
        print("Foo")
    elif a % 3 != 0 and a % 5 == 0 and a != 0:
        print("Bar")
    else:
        print("Something is wrong")
        






