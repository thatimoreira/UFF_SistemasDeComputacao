# Programa completo sem variáveis globais

# Subprogramas
def mult(x, y):
    z = 0
    for u in range(x):
        z = z + y
    return z


# Programa Principal
w = mult(20, 200) + 10
# Neste ponto, w vale 4010
print(w)
w = mult(10, 100) + 20
# Neste ponto, w vale 1020
print(w)
