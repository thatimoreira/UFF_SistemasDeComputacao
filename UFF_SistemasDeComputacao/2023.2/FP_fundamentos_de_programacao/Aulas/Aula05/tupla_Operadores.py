print("\n1. Concatenação: a + b")
print("   Operador infixado que gera uma nova tupla a partir do conteúdo da\n   "
      "primeira (a), seguido do conteúdo da segunda (b).")

print("\n---------------------------------------------------------------------\n")
print("2. Replicação: a * n")
print("   Operador que gera uma nova tupla a partir do conteúdo da primeira (a),\n   "
      "seguido pela repetição do mesmo conteúdo n – 1 vezes. ")

print("\n---------------------------------------------------------------------\n")
print("3. Fatiamento: a[posição inicial : posição final + 1]")
print("   Operador que gera uma nova tupla a partir de um subconjunto de elementos\n   "
      "contidos na tupla original (a).")

print("\n---------------------------------------------------------------------\n")
print("4. Operadores de atribuição incremental: a += b   ou   a *= n")
print("   Equivale aos operadores de concatenação e replicação, porém é atribuído à\n   "
      "variável (a) a referência para a nova tupla gerada.")

print("\n---------------------------------------------------------------------\n")
print("5. Operadores de comparação: <,  <=,  ==,  !=,  >  ou  >=")
print("   Comparação item a item e, recursivamente, para itens aninhados.")

print("\n---------------------------------------------------------------------\n")
print("6. Teste de associação: in e not in")
print("Verifica a pertinência de um valor em uma tupla.")

print("\n---------------------------------------------------------------------\n")
print("Exemplo")
print(">> Especificação do Problema:")
print("     Construa uma lista de compras representada por um vetor de tuplas, onde cada\n"
      "     tupla contém o nome do produto, a quantidade e o preço unitário definidos pelo\n"
      "     usuário. Mostre na saída padrão o conteúdo da lista e o total gasto na compra.")
print(">> Formato da Entrada:")
print("     Cada produto comprado é especificado pelo usuário em três linhas. A primeira\n"
      "     contém o nome do produto, a segunda contém a quantidade e a terceira o preço\n"
      "     unitário. O produto com nome “Fim” representa o término da lista e não deve ser\n"
      "     incluído na mesma. ")
print()
print(">> Exemplo de Entrada:")
print("     Fruta do Conde\n     3\n     7.80\n     Leite\n     2\n     3.99\n     Fim")
print("\n---------------------------------------------------------------------\n")


# Subprograma
def preencher():
    itens = []
    nome = input("Nome do Produto: ")
    while nome != "Fim":
        qtd = int(input("Quantidade: "))
        preco = float(input("Preco Unitario: "))
        itens.append((nome, qtd, preco))
        nome = input("Nome do Produto: ")
    return itens


# Subprograma
def processa(itens):
    total = 0.0
    for (nome, qtd, preco) in itens:
        total += qtd * preco
        print("Nome:", nome, " | Quantidade:", qtd, " | Preço:", preco)
    print("Total Gasto:", total)
    return None


# Programa Principal
compras = preencher()
print("\n-------------------------------------------------------------------\n")
processa(compras)
