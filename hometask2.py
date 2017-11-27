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
        
#Task7
x = [1, 33, 7, 18, 7, 9, 11, -5, 0, 12, 32]

count = x[0]

for i in range(len(x)):
    if x[i] > count:
        count = x[i]

print(count)

#Task8
x = [1, 33, 7, 18, 7, 9, 11, -5, 0, 12, 32]

count = x[0]

for i in range(len(x)):
    if x[i] < count:
        count = x[i]

print(count)

#Task9
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



