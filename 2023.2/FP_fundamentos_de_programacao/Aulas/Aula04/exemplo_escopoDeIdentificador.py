# Programa Completo

global x  # x escopo global


# Subprogramas
def p(n):  # n escopo local a p
    y = 13  # y escopo local a p
    # Neste ponto, x, y e n são conhecidos
    return x + y + n


def q(m):  # m escopo local a q
    z = 3  # z escopo local a q# z escopo local a q
    # Neste ponto, x, z e m são conhecidos
    return m ** z - x * m


# Programa Principal
x = 26
# Neste ponto, apenas x, p e q são conhecidos
print(p(x), q(2 * x + p(3)))
