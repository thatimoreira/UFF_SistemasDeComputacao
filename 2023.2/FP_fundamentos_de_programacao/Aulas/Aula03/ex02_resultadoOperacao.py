valores = input("Informe dois nºs inteiros positivos: ").split()
x = int(valores[0])
y = int(valores[1])
operacao = input("Informe o operador(+, -, *, / ou **): ")

resultado = 0

if operacao == "+":
    resultado = x + y
elif operacao == "-":
    resultado = x - y
elif operacao == "*":
    resultado = x * y
elif operacao == "/":
    resultado = x / y
elif operacao == "**":
    resultado = x ** y

print("%d %s %d = %.2f" % (x, operacao, y, resultado))
