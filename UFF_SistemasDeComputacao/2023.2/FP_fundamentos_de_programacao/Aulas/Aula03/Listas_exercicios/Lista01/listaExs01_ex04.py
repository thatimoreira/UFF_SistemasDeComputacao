# Beecrowd: 1064
positivos = 0
somaPositivos = 0

for i in range(6):
    n = float(input())
    if n > 0:
        positivos += 1
        somaPositivos += n

mediaPositivos = somaPositivos / positivos

print("%d valores positivos" % positivos)
print("%.1f" % mediaPositivos)
