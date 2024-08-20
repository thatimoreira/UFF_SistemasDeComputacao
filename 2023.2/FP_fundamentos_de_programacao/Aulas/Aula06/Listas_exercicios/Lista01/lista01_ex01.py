# Beecrowd: 1048
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1048

def calcularAumentoSalario(salario):

    if 0 <= salario <= 400.00:
        salarioReajustado = salario * 1.15
    elif 400.01 <= salario <= 800.00:
        salarioReajustado = salario * 1.12
    elif 800.01 <= salario <= 1200.00:
        salarioReajustado = salario * 1.1
    elif 1200.01 <= salario <= 2000.00:
        salarioReajustado = salario * 1.07
    elif salario > 2000.00:
        salarioReajustado = salario * 1.04

    return salarioReajustado


# Programa Principal
salarioFuncionario = float(input())
novoSalario = calcularAumentoSalario(salarioFuncionario)
reajusteGanho = novoSalario - salarioFuncionario
percentualReajuste = (reajusteGanho / salarioFuncionario) * 100
print("Novo salario: %.2f" % novoSalario)
print("Reajuste ganho: %.2f" % reajusteGanho)
print("Em percentual: %.0f %%" % percentualReajuste)
