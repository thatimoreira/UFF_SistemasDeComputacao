'''
Especificação do Problema:
Faça um programa para ler, do teclado, dez números reais e escrevendo-os, na saída padrão (vídeo), em ordem crescente.

Metodologia para a Solução: 
1.Caso não exista, crie um projeto do qual seu programa fará parte;
2.Dentro do projeto, crie um nome para o programa: exemplo.py;
3. Identifique a “necessidade” de constantes: TAM;
4.Declare as variáveis necessárias: numeros;
5. Identifique “macro” operações a serem realizadas: ler, ordenar e escrever;
6. Faça os cabeçalhos e blocos vazios (“stubs”) das operações;
7. Salve o programa novamente e execute-o;
8. Escreva o corpo da primeira operação (escolhida por facilidade);
9. Salve e execute o programa;
10. Escreva o corpo de uma próxima operação (escolhida por facilidade);
11. Salve e execute o programa;
12. Escreva o corpo da próxima operação (escolhida por facilidade);
'''

# Subprogramas 
def escrever(valores):
    for item in valores:
         print(item, end=" ")
    print() 
    return None

def ler(valores):
    for ind in range(len(valores)):
        valores[ind] = float(input("vs[" + str(ind+1) + "] = "))
    return None

def ordenar(valores):
    # Função Interna: ondeMenor
    def ondeMenor(vals, inicio):
        posMenor = inicio
        for p in range(inicio+1, len(vals)):
            if vals[p] < vals[posMenor]:
                posMenor = p
        return  posMenor
            
    for ind in range(len(valores)-1):
        posicao = ondeMenor(valores, ind)
        temp = valores[ind]
        valores[ind] = valores[posicao]
        valores[posicao] = temp
    return None

# Programa Principal - exemplo
TAM = 10
numeros = [0.0] * TAM         # Cria o vetor com dez valores zero
ler(numeros)
escrever(numeros)
ordenar(numeros)
escrever(numeros) 