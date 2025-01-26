# Super Módulo parte 2

Os exercícios a seguir são baseados na lista de dicionários a seguir:

```python
dados = [
    {
        "id": 1,
        "nome": "João",
        "idade": 25,
        "habilidades": ["Python", "SQL", "HTML"],
        "empregado": True,
        "endereco": {"cidade": "São Paulo", "estado": "SP", "pais": "Brasil"},
        "salario": 3500.0,
        "projetos": [
            {"nome": "Sistema de Vendas", "duracao_meses": 6, "concluido": True},
            {"nome": "Site Institucional", "duracao_meses": 3, "concluido": False},
        ],
        "notas": {"av1": 8.5, "av2": 9.0}
    },
    {
        "id": 2,
        "nome": "Maria",
        "idade": 30,
        "habilidades": ["JavaScript", "CSS"],
        "empregado": False,
        "endereco": {"cidade": "Rio de Janeiro", "estado": "RJ", "pais": "Brasil"},
        "salario": None,
        "projetos": [
            {"nome": "E-commerce", "duracao_meses": 12, "concluido": True},
        ],
        "notas": {"av1": None, "av2": 7.5}
    },
    {
        "id": 3,
        "nome": "Carlos",
        "idade": 28,
        "habilidades": ["Java", "C++", "Python"],
        "empregado": True,
        "endereco": {"cidade": "Belo Horizonte", "estado": "MG", "pais": "Brasil"},
        "salario": 4000.0,
        "projetos": [],
        "notas": {"av1": 9.5, "av2": 8.0}
    },
    {
        "id": 4,
        "nome": "Ana",
        "idade": None,
        "habilidades": [],
        "empregado": False,
        "endereco": {"cidade": None, "estado": None, "pais": None},
        "salario": None,
        "projetos": [],
        "notas": {}
    },
    {
        "id": 5,
        "nome": "Pedro",
        "idade": 40,
        "habilidades": ["C#", "JavaScript"],
        "empregado": True,
        "endereco": {"cidade": "Curitiba", "estado": "PR", "pais": "Brasil"},
        "salario": 5000.0,
        "projetos": [
            {"nome": "ERP Corporativo", "duracao_meses": 18, "concluido": True},
            {"nome": "Integração de APIs", "duracao_meses": 4, "concluido": True},
        ],
        "notas": {"av1": 10.0, "av2": 9.5}
    }
]
```

1. **Exibindo detalhes**
   - Percorra a lista e exiba o nome, idade e cidade de cada pessoa no formato:
     ```
     João, 25 anos, São Paulo
     Maria, 30 anos, Rio de Janeiro
     ```

2. **Filtrando por projeto concluído**
   - Crie uma lista com os nomes de pessoas que têm **ao menos um projeto concluído**.

3. **Calculando média de notas**
   - Para cada pessoa que possui notas válidas, calcule a média das notas (`av1` e `av2`) e adicione-a como uma nova chave `"media"` no dicionário de cada pessoa.

4. **Habilidades mais comuns**
   - Gere uma contagem de quantas vezes cada habilidade aparece na lista.

5. **Filtrando por salário**
   - Crie uma lista com as pessoas que possuem salário maior ou igual a 4000. Exiba apenas o nome e o salário.

6. **Criando ranking**
   - Crie um ranking das pessoas baseado na soma da duração de seus projetos. Quem tem mais meses de projetos aparece primeiro.

7. **Ordenação complexa**
   - Ordene a lista com base nos seguintes critérios:
     1. Empregados aparecem primeiro.
     2. Dentro dos empregados, ordene por salário (decrescente).
     3. Não empregados aparecem depois, ordenados por idade (crescente).

8. **Análise de projetos**
   - Exiba o número total de projetos (concluídos e não concluídos) de cada pessoa no formato:
     ```
     João: 2 projetos
     Maria: 1 projeto
     ```

9. **Salário por estado**
   - Agrupe os salários por estado e exiba a soma total de salários para cada estado.

10. **Criando uma lista resumida**
    - Crie uma nova lista que contenha apenas os seguintes campos:
      - Nome
      - Habilidades
      - Cidade
      - Total de projetos concluídos

11. **Verificando dados incompletos**
    - Crie uma lista com os nomes das pessoas que possuem **valores nulos** em qualquer campo.

12. **Exibindo habilidades formatadas**
    - Exiba as habilidades de cada pessoa em uma linha separada no formato:
      ```
      João: Python, SQL, HTML
      Maria: JavaScript, CSS
      ```

13. **Número médio de projetos**
    - Calcule o número médio de projetos (concluídos ou não) entre todas as pessoas da lista.

14. **Atualizando dados de endereço**
    - Atualize todos os dicionários para adicionar a chave `"regiao"` com o valor:
      - `"Sudeste"` para estados SP, RJ e MG.
      - `"Sul"` para o estado PR.
      - `None` para estados desconhecidos.

15. **Detalhes do maior salário**
    - Identifique a pessoa com o maior salário e exiba todos os detalhes dela, incluindo os projetos.

16. **Pessoas com habilidades específicas**
    - Crie uma lista com os nomes das pessoas que possuem tanto "Python" quanto "JavaScript" como habilidades.

17. **Adicionando status ao projeto**
    - Adicione uma nova chave `"status"` a cada projeto com os valores:
      - `"Finalizado"` se concluído for `True`.
      - `"Em andamento"` se concluído for `False`.

18. **Resumo geral**
    - Crie um resumo geral que exiba:
      - Número total de pessoas na lista.
      - Quantas estão empregadas.
      - Quantos projetos concluídos no total.
      - A média salarial.

19. **Transformando a estrutura**
    - Converta a lista de dicionários em um único dicionário onde:
      - A chave é o nome da pessoa.
      - O valor é outro dicionário contendo as chaves "idade", "empregado" e "projetos".

20. **Removendo pessoas sem salário**
    - Crie uma nova lista excluindo todas as pessoas cujo salário seja `None`.
