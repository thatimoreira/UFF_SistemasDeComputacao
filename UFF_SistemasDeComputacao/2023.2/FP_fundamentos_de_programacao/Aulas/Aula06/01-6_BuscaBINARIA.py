# BUSCA BINÁRIA

# Subprogramas
def preencher(valores):
    for ind in range(len(valores)):
        valores[ind] = int(input("Elemento[" + str(ind) + "]="))
    return None


def buscaElemento(valores, procurado):
    inicio = 0
    fim = len(valores) - 1
    meio = (inicio + fim) // 2
    while (inicio < fim) and (procurado != valores[meio]):
        if procurado > valores[meio]:
            inicio = meio + 1
        else:
            fim = meio -1
        meio = (inicio + fim) // 2
    if procurado != valores[meio]:
        local = -1
    else:
        local = meio
    return local


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

numeros.append(dado)  # coloca o procurado no final: o sentinela

# onde: o local no vetor onde dado foi encontrado ou -1 se não encontrado
onde = buscaElemento(numeros, dado)

escreverResposta(dado, onde)
