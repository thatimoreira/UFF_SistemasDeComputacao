n = int(input())

def fat(n):
    if n == 0:                  # Condição de parada    
        return 1
    else:
        return n * fat(n - 1)   # Chamada recursiva

print("%d! = %d" %(n, fat(n)))