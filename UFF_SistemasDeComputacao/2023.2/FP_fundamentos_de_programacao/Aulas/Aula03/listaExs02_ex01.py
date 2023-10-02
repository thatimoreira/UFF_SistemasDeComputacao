'''
Beecrowd: 1073
'''

n = int(input())

for i in range(2, n+1, 2):
    resultado = i ** 2
    print("%d^2 = %d" %(i, resultado), end="\n")