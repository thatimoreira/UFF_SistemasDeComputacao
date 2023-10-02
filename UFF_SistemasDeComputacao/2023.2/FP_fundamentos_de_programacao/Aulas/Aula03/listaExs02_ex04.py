# Beecrowd: 1133

x = int(input())
y = int(input())

inicio = 0
limite = 0

if x < 0 or y < 0:
    print()
elif x < y or x == y:
    tamanho = y - x
    inicio = x
    limite = y
else:
    tamanho = x - y
    inicio = y
    limite = x

for n in range(inicio, limite):
    if n % 5 == 2 or n % 5 == 3:
        print(n)
