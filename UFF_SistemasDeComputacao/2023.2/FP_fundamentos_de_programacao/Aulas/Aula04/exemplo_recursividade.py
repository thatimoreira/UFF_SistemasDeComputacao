n = int(input())


def fat(numero):
    if numero == 0:  # Condição de parada
        return 1
    else:
        return numero * fat(numero - 1)  # Chamada recursiva


print("%d! = %d" % (n, fat(n)))
