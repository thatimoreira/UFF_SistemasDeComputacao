'''
Beecrowd: 1151
'''

n = int(input())

fibonacci = []
fibonacci.append(0)
fibonacci.append(1)

if 0 < n < 46:
    if n == 1:
        print(fibonacci[0])
    elif n == 2:
        print(fibonacci[0])
        print(fibonacci[1])

    else:
        print(fibonacci[0])
        print(fibonacci[1])
        for i in range(2, n):
            soma = fibonacci[i - 2] + fibonacci[i - 1]
            fibonacci.append(soma)
            print(fibonacci[i])
