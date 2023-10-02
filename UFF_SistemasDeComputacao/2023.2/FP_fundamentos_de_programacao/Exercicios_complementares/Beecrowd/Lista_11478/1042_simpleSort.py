n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

numbers = [n1, n2, n3]
sortedNumbers = [n1, n2, n3]
length = 3

for i in range(length - 1):
    for j in range(length - i - 1):
        if sortedNumbers[j] > sortedNumbers[j + 1]:
            temp = sortedNumbers[j]
            sortedNumbers[j] = sortedNumbers[j + 1]
            sortedNumbers[j + 1] = temp

for i in range(length):
    print(sortedNumbers[i])

print()

for i in range(length):
    print(numbers[i])