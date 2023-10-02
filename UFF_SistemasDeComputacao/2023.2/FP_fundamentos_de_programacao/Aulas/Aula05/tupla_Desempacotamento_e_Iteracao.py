# 1) O conteúdo de tuplas pode ser facilmente atribuído a variáveis isoladas por meio de desempacotamento.
print("1.1")
nome, idade = ("Maria José", 39)
print(nome)
print(idade)

print()
print("OU")
print()

print("1.2")
(nome, idade) = ("Maria José", 39)
print(nome)
print(idade)

print("\n--------------------------------\n")

# 2) É possível iterar sobre os itens de uma tupla.
print("2")
olhos = ("castanhos", "verdes", "azuis", "pretos")
for cor in olhos:
    print(cor)
