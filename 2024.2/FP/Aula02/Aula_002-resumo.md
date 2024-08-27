# Variáveis, Tipos e Comandos Básicos

### Variáveis
Área de memória que mantém um valor que pode ser mudado

<br>

### Nomenclatura de variáveis
Sequência de caracteres iniciada por letra minúscula.
Ex: nota, saldo, deposito, saque, casa13Buzios

<br>

### Padronização da nomenclatura de variáveis nesta disciplina
- Não deve ter acentos
- Possuir apenas caracteres alfanuméricos
- Camel case -> Ex: minhaNota, notaTurma, cartoesAmarelos, cartoesVermelhos
<br>

### Tipos Básicos (embutidos)
- São imutáveis -> estão em uma área da memória e não trocarão seus valores
  <br>
  <br>
- Tipos Integrais
  - Inteiro: **int**
    - Pode ter centenas de dígitos, limitado apenas pela memória do computador
    - Padrão: decimal. Mas pode usar outras bases como binária(iniciada c/**0b**), octal (iniciada c/**0o**) ou hexadecimal (iniciada com **0x**)
      <br>
      <br>
  - Lógico (ou booleano): **bool**
    - 0 -> **False**
    - 1 -> **True**
      <br>
      <br>
  - Ponto-Flutuante
    - Ponto-flutuante: **float**
    - Número complexo: **complex** ->representado por um par de números ponto-flutuantes
      <br>
      <br>
  - String: **str**
    - Sequência de caracteres unicode entre aspas simples ou duplas
    <br>

### Conversão de tipos
- **int**: String, booleano ou ponto-flutuante para inteiro
- **float**: String, booleano ou inteiro para ponto-flutuante
- **bool**: String, inteiro ou ponto-flutuante para booleano
- **str**: Booleano, inteiro ou ponto-flutuante para String
<br>

### Linguagem de Tipagem Dinâmica
Exemplo de uma sequência de atribuição de valores à uma variável:

- x = 10      -> x referencia uma área de memória que contém o valor 10
- x = "Maria" -> x referencia uma área de memória que contém uma String
- x = True    -> x referencia uma área de memória que contém o valor True
- x = 13.25   -> x referencia uma área de memória que contém o valor 13.25
- y = 1.75    -> y tem uma área de memória própria com o valor 1.75
- x = x + y   -> Agora temos uma nova área de memória que vai receber o valor 15
<br>

### Diagramas sintáticos
- Atribuição Simples: **Variável = Expressão**
  <br>
- Atribuição Múltipla: **Var1, ..., VarN = Exp1, ..., ExpN**
<br>

### Expressão
- Especifica o cálculo de um valor
- É definida por operandos e operadores: deposito - saque (operandos: deposito e saque | operador: -)
<br>

### Operando
- Pode ser uma constante, uma variável ou o resultado de uma função
  - Ex: (a + 10) * maior(x, y)  => a: variável | 10: constante | maior(x, y): função
    <br>

### Operador
Pode ser unário ou binário, admite um ou dois operandos, respectivamente
Ex: (-a + 10) * maior(x, y) => operador unário: - | operadores binários: + e *
<br>
- Operadores unários
  - Operador numérico positivo (**+**): operando deve ser umérico => ex: 5.75 (constante real)
  - Operador numérico negativo (**-**): operando deve ser umérico => ex: -a (variável numérica)
  - Operador lógico de negação (**not**): operando deve ser booleano => ex: **not** fim (fim é uma variável booleana)
    <br>
    
- Operadores binários aritméticos
  - Operadores Aditivos:
    - Soma (**+**)
    - Subtração (**-**)
      <br>
      
  - Operadores Multiplicativos:
    - Produto (*)
    - Divisão de ponto flutuante (**/**)
    - Divisão inteira (**//**)
    - Resto da divisão (**%**)
    - Potenciação (**)
  <br>

  - Operadores binários lógicos
    - Disjunção lógica ou soma lógica (**or**)
    - Conjunção lógica ou produto lógico (**and**)
  <br>

  - Operadores binários Relacionais
    - Igual a (**==**)
    - Diferente de (**!=**)<br>
    <br>
    
    - Maior que (**>**)
    - Menor que (**<**)
    - Maior ou igual a (**>=**)
    - Menor ou igual a (**<=**)

O resultado de uma operação relacional é um valor booleano. Exs: <br>
(2 + 2) == 5  **é falso**<br>
(2 + 2) <= 5  **é verdadeiro**
<br>

### Precedência dos operadores
1. Expressão entre Parênteses **()**  -> Maior prioridade
2. Potenciação (**)
3. Unários (**+**, **-**)
4. Binários Multiplicativos (*, /, %, //)
5. Binários Aditivos (**+**, **-**)
6. Relacionais (==, !=, <, >, <=, >=)
7. Lógico **not**
8. Lógico **and**
9. Lógico **or**  -> Menor prioridade

Ex: **5.75 + a % b - 7/8.1** equivale a **5.75 + (a%b) - (7/8.1)**

=> A precedência de  operadores de mesma classe: o da esquerda tem maior precedência<br>
   Ex: **5 * a % b / 8.1 ** equivale a **((5 * a) % b) / 8.1**
<br>
<br>

### Comandos de Saída Padrão
- **print( )**<br>
    - Pula para a próxima linha na saída padrão (vídeo) - quando não possui parâmetro

- **print(** expressão **)**<br>
   - Escreve na saída padrão (vídeo) o resultado da avaliação da expressão<br>
   - Depois pula para a próxima linha

- **print(** exp1, exp2, ..., expN **)**<br>
   - Escreve na saída padrão (vídeo) o resultado da avaliação de cada expressão expNum<br>
   - Depois pula para a próxima linha

- **print(** expressão, **end =** término **)**<br>
   - Escreve na saída padrão (vídeo) o resultado da avaliação da expressão<br>
   - Depois escreve a String de término

- **print(** exp1, exp2, ..., expN, **end =** término**)**<br>
   - Escreve na saída padrão (vídeo) o resultado de cada avaliação de cada expressão expNum
   - Um espaço em branco é escrito entre cada par de expNum
   - Depois pula para a próxima linha
<br>
<br>

### Diagrama Sintático do Comando *print*
![image](https://github.com/user-attachments/assets/53e19a06-13da-4276-ac03-a1cc055d598d)
