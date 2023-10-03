# Beecrowd: 2456 - Cards
# https://www.beecrowd.com.br/judge/en/problems/view/2456?origem=1

# Subprogramas
def lerCartas(entrada):
    tiragem = []

    for i in range(5):
        tiragem.append(int(entrada[i]))

    return tiragem


def ordenarCrescente(cartas):
    ordemCrescente = []  # cópia do vetor de valores de cartas com seus valores ordenados
    pivo = cartas[(len(cartas) // 2)]  # define o pivô, que é o elemento na posição tamanho do vetor//2
    elementosEsquerda = []
    elementoCentral = 0
    elementosDireita = []

    for elemento in cartas:
        if elemento < pivo:
            elementosEsquerda.append(elemento)
        elif elemento > pivo:
            elementosDireita.append(elemento)
        elif elemento == pivo:
            elementoCentral = pivo

    ordemCrescente = elementosEsquerda + [elementoCentral] + elementosDireita

    return ordemCrescente  # vetor com os valores das cartas em ordem crescente


def analisarCartas(cartas, cartasOrdemCrescente):
    is_decrescente = True
    for i in range(len(cartas) - 1):
        if cartas[i] < cartas[i + 1]:
            is_decrescente = False

    if cartas == cartasOrdemCrescente:
        return "C"
    elif is_decrescente:
        return "D"
    else:
        return "N"


# Programa Principal
entrada = input().split()
cartas = lerCartas(entrada)
cartasOrdemCrescente = ordenarCrescente(cartas)
ordenacao = analisarCartas(cartas, cartasOrdemCrescente)
print(ordenacao)
