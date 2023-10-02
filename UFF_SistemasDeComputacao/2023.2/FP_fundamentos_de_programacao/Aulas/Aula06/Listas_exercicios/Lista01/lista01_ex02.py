# Beecrowd: 1180 - Lowest Number and Position
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1180

# Subprogramas
def lerElementos(tamanho):
    entrada = input().split()
    vetor = []

    for elemento in entrada:
        vetor.append(int(elemento))
    return vetor

def buscarMenor(vetor):
    menor = vetor[0]
    posicao = 0

    for i in range(1, n):
        if menor > vetor[i]:
            menor = vetor[i]
            posicao = i

    return menor, posicao

# Programa Principal
n = int(input())
X = lerElementos(n)
menorValor, posicaoMenor = buscarMenor(X)

print("Menor valor: %d" % menorValor)
print("Posicao: %d" % posicaoMenor)
