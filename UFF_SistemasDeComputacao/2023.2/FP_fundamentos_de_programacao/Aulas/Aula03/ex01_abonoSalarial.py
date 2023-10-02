salario = float(input("Informe o salário do(a) funcionário(a): R$ "))
tempoServico = int(input("Informe o tempo de serviço do(a) funcionário(a) em anos: "))

if tempoServico <= 1:
    print("O(a) funcionário(a) não tem direito ao abono salarial.")
elif tempoServico > 1 and tempoServico < 10:
    salario *= 1.1
else:
    salario *= 1.25

print("Salário com abono: R$ %.2f" %salario)