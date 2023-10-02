# No caso de existirem dois identificadores, definidos em escopos diferentes, com o mesmo nome x,
# a ocorrência do nome x estará referenciando aquele com o escopo mais local.


# Programa Completo

global x    # Variável Global x

# Subprograma
def colisao(m):
    x = 8   # Variável Local x
    z = 13
    # Neste ponto, as variáveis x e z locaisa q
    # e o parâmetro m são conhecidos.
    x = x + 1
    # A variável local x foi alterada.
    print(x, z, m*2)    # escreve 9, 13 e 2000
    return None

# Programa Principal
# # Neste ponto, apenas variável global x é conhecida,  além do nome da função.
x = 57
colisao(1000)
print(x)    # escreve 57