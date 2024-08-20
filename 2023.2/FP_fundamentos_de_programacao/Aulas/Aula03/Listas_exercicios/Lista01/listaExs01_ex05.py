# Beecrowd: 1072

n = int(input())

noIntervalo = 0
foraIntervalo = 0

for i in range(n):
    num = int(input())
    if 10 <= num <= 20:
        noIntervalo += 1
    else:
        foraIntervalo += 1

print("%d in" % noIntervalo)
print("%d out" % foraIntervalo)
