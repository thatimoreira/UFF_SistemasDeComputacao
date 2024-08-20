# Estado do Jogo da Velha

# O valor 0 representa que a célula está vazia, ou seja, ainda não usada.
tabuleiro = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
print(tabuleiro)
tabuleiro[1][1] = 1  # o jogador 1 marcou a célula central
print(tabuleiro)
tabuleiro[0][2] = 2  # o jogador 2 marcou a célula superior direita
print(tabuleiro)
tabuleiro[0][0] = 1  # o jogador 1 marcou a célula superior esquerda
print(tabuleiro)
tabuleiro[2][2] = 2  # o jogador 2 marcou a célula inferior direita
print(tabuleiro)
