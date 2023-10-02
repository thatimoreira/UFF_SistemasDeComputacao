num = int(input("Digite um valor inteiro e positivo: "))

fat = 1
for i in range(1, num+1):
    fat *= i
print("%d! = %d" %(num, fat))