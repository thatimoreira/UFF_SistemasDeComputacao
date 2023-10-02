# BUSCA SIMPLES (utilizando for com saída rápida)

# Subprogramas
def preencher(valores):
    for ind in range(len(valores)):
        valores[ind] = int(input("Elemento[" + str(ind) + "]="))
    return None


def buscaElemento(valores, procurado):
    for indice in range(len(valores)):
        if valores[indice] == procurado:
            return indice  # retorna ao encontrar o local
    return -1  # retorna -1 se terminar sem encontrar


def escreverResposta(valor, pos):
    if pos < 0:
        print(valor, "não foi encontrado")
    else:
        print(valor, "foi encontrado na posição", pos)
    return


# Programa Principal de Busca
numeros = [0] * 10  # Cria o vetor numeros zerado, com tamanho n = 10
preencher(numeros)

# dado: o elemento a ser procurado
dado = int(input("Escolha valor a ser procurado: "))

# onde: o local no vetor onde dado foi encontrado ou -1 se não encontrado
onde = buscaElemento(numeros, dado)

escreverResposta(dado, onde)
