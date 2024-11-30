# Aula 05: Funções II

1. Crie uma função `imprime_args` que aceite qualquer número de argumentos posicionais e, no final, imprime cada argumento em uma nova linha.
   > Exemplo: `imprime_args('olá', 'alunos', ['vamos', 'praticar'])` deve retornar:
   ```
   olá
   alunos
   ['vamos', 'praticar']
   ```

2. Crie uma função `soma_numeros` que receba qualquer número de números e retorne a soma deles.
    ```python
    def somar_numeros(*args):
      #escreva seu código aqui
    ```

3. Escreva uma função `junta_listas` que aceite várias listas como argumentos e retorne uma única lista contendo todos os elementos.
    ```python
    def junta_listas(*listas):
      #escreva seu código aqui
    ```
4. Defina uma função `imprime_chave_e_valor` que aceite argumentos nomeados e imprima cada par chave-valor.
    ```python
    def imprime_chave_e_valor(*kwargs):
      #escreva seu código aqui
    ```
5. Crie uma função `descrever_objeto` que tenha um argumento obrigatório, um argumento padrão e aceite argumentos nomeados adicionais. Imprima o argumento obrigatório, o valor padrão e os argumentos nomeados.
    ```python
    def descrever_objeto(nome, categoria="desconhecida", **kwargs):
      #escreva seu código aqui
    ```
6. Crie uma função `filtra_pares` que aceite qualquer quantidade de números inteiros e retorne apenas os números pares.
    ```python
    def filtra_pares(*args):
      #escreva seu código aqui
    ```
7. Crie uma função `uniao_intersecao` que aceite vários conjuntos e retorne a união e a interseção deles.
    ```python
    def uniao_intersecao(*args):
      #escreva seu código aqui
    ```
8. Crie uma função que aceite conjuntos e realize uma operação matemática com base em um argumento nomeado.
    ```python
    def operacao_com_conjuntos(operacao, *args):
      #escreva seu código aqui
    ```
9. Crie uma função lambda que recebe uma lista de números e retorna o quadrado de cada um deles. Use-a com a função `map` para aplicar em uma lista de números.

    ```python
    numeros = [1, 2, 3, 4, 5]
    # Resultado esperado: [1, 4, 9, 16, 25]
    ```
10. Escreva uma função lambda para filtrar números pares de uma lista usando a função `filter`.
    ```python
    numeros = [10, 15, 20, 25, 30]
    # Resultado esperado: [10, 20, 30]
    ```
11. Crie uma função lambda para encontrar a string mais longa em uma lista de strings. Use a função `max` com a lambda
    ```python
    palavras = ["maçã", "banana", "cereja", "tâmara"]
    # Resultado esperado: "banana"
    ```
# Desafios maiores (boa sorte!)
1. Escreva uma função lambda para combinar duas listas em um dicionário, onde a primeira lista será usada como chave e a segunda como valor.
    ```python
    chaves = ['a', 'b', 'c']
    valores = [1, 2, 3]
    # Resultado esperado: {'a': 1, 'b': 2, 'c': 3}
    ```
2. Use uma função lambda para elevar cada número de uma lista a uma potência personalizada fornecida.

    ```python
    numeros = [2, 3, 4, 5]
    potencia = 3
    # Resultado esperado: [8, 27, 64, 125]
    ```
3. Escreva uma função que aceite várias strings e as agrupe em um dicionário pela primeira letra.
    ```python
    agrupar_por_letra("abelha", "amora", "caju", "constância", "estudo", "persistir")
    #resultado esperado: {a: ["abelha", "amora"], c:["caju", "constância"], e: ["estudo"], p:["persistir"]}
    ```
4. Escreva uma função que receba vários dicionários como argumentos nomeados e os mescle em um único dicionário:
    ```python
    def mesclar_dicionarios(**kwargs):
    #escreva seu código aqui
    ```
5. Use as funções `map()`, `filter()` e `reduce()` juntas:
- Comece com uma lista de números.
- Eleve ao quadrado cada número usando `map`.
- Filtre os números cujo quadrado seja maior que 50 usando `filter`.
- Encontre o produto dos números restantes usando `reduce`.
    > Exemplo: com a lista `[2, 5, 8, 10, 12]` o retorno deve ser 921600
6. Dada a lista de dicionários a seguir, crie uma função lambda `arrecadacao_total` que calcula o somatório de `faturamento` em cada setor.
    ```python
    arrecadacao = [
    {
        "setor": "arquibancada alta",
        "faturamento": 15780.23
    },
    {
        "setor": "cadeira",
        "faturamento": 15900.23
    },
    {
        "setor": "visitante",
        "faturamento": 12950
    },
    ]
    ```
