# Super módulo: desafios

1. Crie uma função que verifique qual item da lista é maior do que 100. Imprima a mensagem `Encontrei um número maior que 100: x` sendo `x` o valor do número. Caso não se cumpra a condição, retorne `False`.
   > Exemplo: dada a lista `[7, 5, 159, 30, 12, 15]`, deve-se retornar `encontrei um número maior do que 100: 159`

2. Crie um programa que verifica se uma palavra é um anagrama de outra palavra
   > Exemplo: `anagrama("iracema", "america")` deve retornar `True`

3. Crie uma função fizzbuzz, que recebe uma lista e imprime na tela `fizz` para cada número que for divisível por 3, `buzz` para cada número divisível por 5 e `fizzbuzz` para cada número divisível por 3 e por 5.
   > Exemplo:  `[2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15, 17, 22, 24, 30]` como argumento deverá retornar `2 fizz 4 buzz fizz 7 8 fizz fizz 14 fizzbuzz 17 22 fizz fizzbuzz`(separado linha a linha)
4. Crie uma função que realiza a seguinte impressão no seu terminal:
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```
5. Crie uma função que recebe um nome e retorne sempre o primeiro e o último nome, separados por vírgula
    > Exemplo: dado o nome `'Lauro Lyra Aguiar'`, a função deve retornar `Aguiar, Lauro`. Se o nome for `'Carlos Alberto'`, deve retornar `Alberto, Carlos`

6. Crie um programa que retorne uma lista de `n` elementos, sendo preenchida por `"bem me quer"` e `"mal me quer"` de forma alternada. 

7. Considerando a lista de dicionários abaixo, escreva uma função que recebe uma lista nesse formato e retorna o nome dos jogadores que tem o valor `capitao` verdadeiro
```python
jogadores = [
  {
    "nome": 'deyverson',
    "numero": 9,
    "posicao": 'atacante',
    "capitao": False
  },
  {
    "nome": 'hulk'
    "numero": 7
    "posicao": 'atacante',
    "capitao": True
  },
  {
    "nome": 'everson',
    "numero": 1,
    "posicao": 'goleiro',
    "capitao": True
  }
]
```

8. Escreva um programa que encontre o maior e o menor número em uma lista sem usar funções integradas como `max` ou `min`.
   
9.  Escreva um programa que retorne uma lista de números na sequência de fibonacci com `n` elementos
    > Exemplo: `fibonacci(3)` deve retornar `[0, 1, 1]`

10. Escreva um programa que verifique se uma lista está ordenada de forma crescente ou não. 

11. Escreva um programa que receba 16 números de um cartão de crédito e retorne uma string com `*` no lugar de cada dígito, exceto os quatro últimos, que deverão aparecer.
    >Exemplo: `oculta_cartao(0000000000001234)` deve retornar `************1234` 

12.  Um triângulo é composto de três linhas: `linha_a`, `linha_b` e `linha_c`. Crie uma função chamada `verifica_triangulo` que deverá receber as três linhas como parâmetro e retornar se é possível formar um triângulo com os valores apresentados de cada linha. Para tanto, tenha em mente algumas considerações:

- Para que seja possível formar um triângulo, é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.

- Para obter o valor absoluto de um número em Python, pesquise pela função `abs()`.

- O retorno da sua função deverá ser um booleano.
   >Exemplo: o retorno de `verifica_triangulo(10, 14, 8)` deverá ser `True`.

13. Dada a lista de dicionários a seguir, crie uma função `arrecadacao_total` que calcula o somatório de `faturamento` em cada setor.
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
14.  Escreva uma função que aceite várias strings e as agrupe em um dicionário pela primeira letra.
  ```python
  agrupar_por_letra("abelha", "amora", "caju", "constância", "estudo", "persistir")
  #resultado esperado: {a: ["abelha", "amora"], c:["caju", "constância"], e: ["estudo"], p:["persistir"]}
  ```
15.  Escreva um programa que, dada uma lista de números inteiros, encontre o comprimento da maior subsequência contínua de números consecutivos presentes na lista.
      >Exemplo: `conta_subsequencia([1, 9, 3, 10, 4, 20, 2, 11, 12, 13, 14, 15, 17, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29])` espera um retorno de `8`
