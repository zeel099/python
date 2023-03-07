matOne = []
print("Enter the elements: ")
for i in range(2):
    matOne.append([])
    for j in range(2):
        num = int(input())
        matOne[i].append(num)

matTwo = []
print("Enter the elments: ")
for i in range(2):
    matTwo.append([])
    for j in range(2):
        num = int(input())
        matTwo[i].append(num)

matThree = []
for i in range(2):
    matThree.append([])
    for j in range(2):
        matThree[i].append(matOne[i][j]+matTwo[i][j])

print("\nAddition  Matrix is:")
for i in range(2):
    for j in range(2):
        print(matThree[i][j], end=" ")
    print()