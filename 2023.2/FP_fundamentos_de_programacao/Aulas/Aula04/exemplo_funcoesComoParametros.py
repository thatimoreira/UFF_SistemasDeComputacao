# Programa Completo

# Subprogramas
def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)


def fib(num):
    if 1 <= num <= 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


def soma(f, n):
    # Esta função soma os n primeiros valores de uma dada função f
    parcial = 0
    for ind in range(1, n + 1):
        parcial = parcial + f(ind)
        return parcial


# Programa Principal
total = soma(fatorial, 10) + soma(fib, 10)
print(total)
