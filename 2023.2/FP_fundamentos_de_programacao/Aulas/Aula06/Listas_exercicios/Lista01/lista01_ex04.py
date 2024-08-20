# Beecrowd: 2455 - Gangorra
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2455

# Subprogramas
def lerPesosComprimentos(pesosComprimentos):
    pcEsq, cgEsq, pcDir, cgDir2 = pesosComprimentos.split()   # separa os pesos das crianças e comprimento das gangorras
    return pcEsq, cgEsq, pcDir, cgDir2


def analisarEquilibrioGangorra(p1, c1, p2, c2):
    ladoEsquerdo = int(p1) * int(c1)
    ladoDireito = int(p2) * int(c2)

    comparacaoLados = ladoEsquerdo - ladoDireito

    if ladoEsquerdo == ladoDireito:
        print(0)
    elif ladoEsquerdo > ladoDireito:
        print(-1)
    else:
        print(1)
    return comparacaoLados



# Programa Pincipal
pc = input()
p1, c1, p2, c2 = lerPesosComprimentos(pc)
equilibrio = analisarEquilibrioGangorra(p1, c1, p2, c2)
