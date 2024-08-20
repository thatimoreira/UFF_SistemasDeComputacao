# BUSCA do MENOR e MAIOR elementos

# Subprogramas
def preencher(valores):
    for ind in range(len(valores)):
        valores[ind] = int(input("Elemento[" + str(ind) + "]="))
    return


def buscarMenorMaiorElementos(valores):
    menor = valores[0]
    maior = valores[0]
    for indice in range(1, len(valores)):
        if menor > valores[indice]:
            menor = valores[indice]
        elif maior < valores[indice]:
            maior = valores[indice]
    return [menor, maior]


def escrever(infos):
    print("O menor elemento =", infos[0], "e o maior elemento =", infos[1])
    return None


# Programa Principal de Busca
numeros = [0] * 10  # Cria o vetor numeros zerado, com tamanho n = 10
preencher(numeros)
extremos = buscarMenorMaiorElementos(numeros)
escrever(extremos)
