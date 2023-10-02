'''
Beecrowd: 1114
'''

password = 2002
tentative = int(input())

while tentative != password:
    print("Senha Invalida")
    tentative = int(input())
print("Acesso Permitido")