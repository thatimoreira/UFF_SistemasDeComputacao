# Beecrowd: 1117

somaNotas = 0
notaInvalida = 0
positivo = 0

while notaInvalida < 2:
    nota = float(input())
    decimal = nota - int(nota)
    if nota < 0 or nota > 10:
        print("nota invalida")
        notaInvalida += 1
    else:
        somaNotas += nota
        positivo += 1

print("Positivo: %d" % positivo)

if notaInvalida < 2:
    media = somaNotas / 2
    print("media = %.2f" % media)
