# Aula 04: Funções

1. Crie uma função `ola_mundo`, que não possui parâmetros e, ao ser chamada, retorna a string `'Olá, mundo!'`

2. Crie uma função `saudacoes`, que recebe um nome de pessoa como parâmetro e, ao ser chamada, retorna a string `Olá, x`, sendo `x` o parâmetro q você passou pra função.

3. Crie uma função `soma_dois` que receba dois números como parâmetros e, ao ser chamada, retorne a soma desses dois números.

4. Crie uma função que, ao receber uma idade, verifica se a pessoa é maior ou menor de idade, retornando `É maior de idade` caso positivo e `É menor de idade` caso negativo.

5. Crie uma função que recebe um nome e retorne sempre o primeiro e o último nome, separados por vírgula
    > Exemplo: dado o nome `'Lauro Lyra Aguiar'`, a função deve retornar `Aguiar, Lauro`. Se o nome for `'Carlos Alberto'`, deve retornar `Alberto, Carlos`

6. Crie uma função `calcula_area_quadrado`, que recebe o valor do lado de um quadrado e, ao ser chamada, retorna o total de sua área.

7.  Crie uma função `calcula_area_retângulo` que recebe o valor dos lados de um retângulo e, ao ser chamada, retorna o total de sua área.

8. Crie uma função `converte_dolar` que recebe um valor em dólares e, ao ser chamada, retorna o valor em reais. _dica: adicione uma variável `cotacao_dolar` dentro de sua função._.

9. Escreva uma função com o nome `divide_frase`, a qual receberá uma string e retornará uma array de strings separadas por cada espaço na string original.
   >Exemplo: se a função receber a string `"infinity dfs"`, o retorno deverá ser `['infinity', 'dfs']`.

10. Crie uma função que recebe uma lista de números e, ao ser chamada, retorna uma lista de tamanho idêntico, mas com todos os números multiplicados por três.
    > Exemplo: dada a lista `[2, 3, 4, 5]`, a função deve retornar `[6, 9, 12, 15]`

11. Considerando a lista de dicionários abaixo, escreva uma função que recebe uma lista nesse formato e retorna o nome dos jogadores que tem o valor `capitao` verdadeiro
```
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

12. Crie uma função `calcula_pontos` que receba o número de vitórias e o número de empates e, ao ser chamada, deve retornar a quantidade de pontos que o time marcou em um campeonato. _Para tanto, considere que cada vitória vale 3 pontos e cada empate vale 1 ponto._


# Desafios maiores (boa sorte!)

1. Crie uma função que resolve uma equação de segundo grau - assim definida como `ax² + bx + c = 0`. A função deve receber três parâmetros `a`, `b` e `c` e calcular o delta. Caso o delta seja positivo, retorne a frase `essa equação aceita dois resultados` junto com seus resultados. Caso o delta seja 0, retorne a frase `essa equação aceita um resultado`. Por fim, caso o delta seja negativo, retorne a frase `não existem resultados para essa equação`.

2. Crie uma função chamada `verifica_meia` que recebe um dicionário `ingresso` com as chaves `nome_completo`(string), `cpf`(número) e `estudante`(booleano) e um valor `preco_ingresso`. Quando essa função for chamada, ela deverá verificar o valor da chave `estudante` e o valor de `preco_ingresso`. Se esse valor for verdadeiro, a função deve retornar `Seu ingresso custa [z / 2] reais`. Se for falso, deve retornar `Seu ingresso custa [z] reais`, sendo `[z]` o valor de `preco_ingresso`
    > Exemplo: se a função `verifica_meia(pagante, preco)` recebe um dicionário `{nome: 'Astolfo Borges', cpf: 00000000000, estudante: True}` e o valor `100`, seu retorno deverá ser `Seu ingresso custa 50 reais`
