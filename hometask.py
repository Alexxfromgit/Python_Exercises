# created a file


names = ['Ann', 'Bob', 'Suzan', 'Radonir', 'Fill', 'Sam', 'Al']
ages = [12, 33, 56, 87, 4, 18, 21]
text_a = "Special cases aren't special enough to break the rules."
text_b = "In the face of ambiguity, refuse the temptation to guess."

print(len(names))

print(len(ages))

print(len(text_a))

print(len(text_b))

print(sum(ages))

print(max(ages))

print(min(ages))

print(min(text_a.split(), key=len))

text_b = text_b.replace(',','')
print(max(text_b.split(), key=len))

if text_a.find('special') != 1:
  print('special')
  
if text_b.find('refuse') != 1:
  print('refuse')
  
i = 0
while i <= len(names) and i <= len(ages):
  print(names[i], ' is', str(ages[i]), ' years old')
  i += 1

  
