# Faça um programa para ler, do teclado, uma String contendo zero ou mais operandos numéricos e zero ou mais
# operadores de soma “+”, constituindo uma expressão numérica válida. Seu programa deve avaliar e escrever
# o valor resultante da expressão lida.

# Exemplo:
def avalia(expressao):
    valor = 0
    if expressao != "":
        partes = expressao.split("+")
        for p in partes:
            valor = valor + float(p)
    return valor

# Programa Principal
lida = input("Entre com uma expressão numérica válida: ")
print("{"+lida+"} =", avalia(lida.strip()))
