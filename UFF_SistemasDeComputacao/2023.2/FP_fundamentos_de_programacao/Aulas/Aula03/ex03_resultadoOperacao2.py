valores = input("Informe dois nºs inteiros positivos: ").split()
x = int(valores[0])
y = int(valores[1])
operador = input("Informe o operador(+, -, *, / ou **): ")

if operador == "+":
    resultado = x + y
elif operador == "-":
    resultado = x - y
elif operador == "*":
    resultado = x * y
elif operador == "/":
    resultado = x / y
elif operador == "**":
    resultado = x ** y
else:
    resultado = None
if resultado == None:
    print("%s Operador inexistente!" %operador)
else:
    print("%d %s %d = %.2f" %(x, operador, y, resultado))