# Subprograma
def listaAprovadosReprovados(estudantes, notas, minimo):
    for pos in range(len(estudantes)):
        media = (notas[pos][0]+notas[pos][1]+notas[pos][2])/3
        if media>=minimo:
             print(estudantes[pos], "Aprovado com nota:", media)
    print("----------------------------------------------------------------")
    for pos in range(len(estudantes)):
        media = (notas[pos][0]+notas[pos][1]+notas[pos][2])/3 
        if media<minimo:
            print(estudantes[pos], "Reprovado com nota:", media)
    return None

# Programa Principal
alunos = ["Maria", "Lucas", "Ana", "Juca", "Carlos"]
resultados = [ [7.2, 4.5, 6.1],
              [3.3, 8.5, 4.5],
              [7.8, 6.7, 8.3],
              [4.0, 6.0, 9.2],
              [2.3, 3.4, 4.0]]
print(alunos)
print(resultados)
listaAprovadosReprovados(alunos, resultados, 6.0) 