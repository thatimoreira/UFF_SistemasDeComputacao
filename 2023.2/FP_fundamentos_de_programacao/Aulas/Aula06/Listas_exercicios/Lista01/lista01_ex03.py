# Beecrowd: 2373 - Garçom
# https://www.beecrowd.com.br/judge/en/problems/view/2373?origem=1

# Subprogramas
def lerQtdeLatasCopos(qtdeBandejas):
    bandejasCheias = []  # lista para armazenar as latas e copos de todas as bandejas

    for i in range(qtdeBandejas):
        entrada = input().split()
        bandeja = []

        for elemento in entrada:
            bandeja.append(int(elemento))   # adiciona os elementos da bandeja atual à lista de bandejas

        bandejasCheias.append(bandeja)  # adiciona a bandeja à lista de bandejas

    return bandejasCheias


def calcularQtdeCoposQuebrados(n, bandejas):
    totalCoposQuebrados = 0

    for bandeja in bandejas:
        latas, copos = bandeja   # latas e copos da bandeja atual
        if latas > copos:
            coposQuebrados = copos
            totalCoposQuebrados += coposQuebrados

    return totalCoposQuebrados


# Programa Principal
n = int(input())
bandejas = lerQtdeLatasCopos(n)
qtdeCoposQuebrados = calcularQtdeCoposQuebrados(n, bandejas)
print(qtdeCoposQuebrados)
