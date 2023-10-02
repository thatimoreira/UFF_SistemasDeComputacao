num = int(input("Digite um valor inteiro e positivo: "))

i = 1
fat = 1

while i <= num:
    fat *= i
    i += 1
print("O fatorial de %d é %d" % (num, fat))
