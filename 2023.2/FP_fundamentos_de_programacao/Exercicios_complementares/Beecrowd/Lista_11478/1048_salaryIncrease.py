salario = round((float(input())), 2)
novoSalario = salario

if salario <= 400.00:
    novoSalario = salario * 1.15
    reajuste = novoSalario - salario
    percentual = "15 %"
elif salario <= 800.00:
    novoSalario = salario * 1.12
    reajuste = novoSalario - salario
    percentual = "12 %"
elif salario <= 1200.00:
    novoSalario = salario * 1.10
    reajuste = novoSalario - salario
    percentual = "10 %"
elif salario <= 2000.00:
    novoSalario = salario * 1.07
    reajuste = novoSalario - salario
    percentual = "7 %"
else:
    novoSalario = salario * 1.04
    reajuste = novoSalario - salario
    percentual = "4 %"

print("Novo salario: %.2f" %novoSalario)
print("Reajuste ganho: %.2f" %reajuste)
print("Em percentual: " + percentual)