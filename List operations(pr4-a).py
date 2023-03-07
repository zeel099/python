fruit = ['apple','banana','guavava','strowbary'] 
print('Nested list')
print(fruit)
print('length...')
print(len(fruit))
print(fruit)
fruit.pop(1)
print('Deleting index 1 value')
print(fruit)
fruits = ['grapes','chiku']
print('Concatenation of 2 list')
print(fruit+fruits)
print('Membership')
if "Truck" in fruits:
 print("Yes , It is present")
print('Iteration')
i = 0
while i < len(fruits): 
 print(fruits[i])
 i = i + 1
print('Indexing the list items')
print('Slicing')
print(fruit[0:7])