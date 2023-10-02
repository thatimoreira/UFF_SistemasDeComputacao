# 1) A função tuple() retorna uma tupla vazia.
print("1")
vazio = tuple()  # ou vazio = ( )
print(vazio)
print("------------------------------------")
print()

# 2) Tuplas não vazias podem ser declaradas com ou sem parênteses.
print("2.1")
valores = ("abacaxi", 500, 4.99)
print(valores)

print()

print("2.2")
valores = "abacaxi", 500, 4.99
print(valores)
print("------------------------------------")
print()


# 3) Vetores e Strings podem ser empacotados como tuplas através da função tuple().
print("3.1")
trio = tuple([1, 2, 3])    # ou trio = (1, 2, 3)
print(trio)

print()

print("3.2")
vogais = tuple("aeiou")    # ou vogais = (“a”, “e”, “i”, “o”, “u”)
print(vogais)