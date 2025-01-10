'''1 - Crie uma lista chamada `pessoas` contendo três dicionários. 
Cada dicionário deve ter as chaves `nome` e `idade`, e seus respectivos valores. 
Em seguida, imprima o nome da primeira pessoa.'''
print('crie uma lista de dicionários')
#escreva o código aqui

'''2 - Dada a lista de tuplas `notas = [('João', 8), ('Maria', 7), ('Pedro', 9)]`,
itere sobre a lista e imprima o nome de cada aluno seguido de sua nota.'''
#escreva o código aqui

'''3 - Dado o dicionário `produto = {'nome': 'Caneta', 'preco': 1.5, 'estoque': 100}`,
verifique se o estoque é maior que 50. Se for, imprima "Estoque suficiente".'''
#escreva o código aqui

'''4 - Escreva uma função `tuplas_para_dicionario(lista)` que receba uma lista de tuplas,
onde cada tupla tem dois elementos: chave e valor.
A função deve retornar um dicionário com essas chaves e valores.
Exemplo: 
lista_de_tuplas = [('nome', 'Ana'), ('idade', 25)]
tuplas_para_dicionario(lista_de_tuplas) deve retornar {'nome': 'Ana', 'idade': 25}'''
def tuplas_para_dicionario(lista):
  print('tuplas_para_dicionario(lista)')
  #remova o print acima e escreva o código aqui
#não esqueça de chamar a função (com argumentos, se necessário) aqui abaixo!

'''5 - Escreva uma função `filtrar_por_idade(pessoas, idade_minima)` que receba uma lista de dicionários
(como na questão 1) e uma idade mínima.
A função deve retornar uma nova lista contendo apenas as pessoas com idade maior ou igual à idade mínima.
Exemplo: 
pessoas = [{'nome': 'Ana', 'idade': 25}, {'nome': 'Bruno', 'idade': 30}, {'nome': 'Clara', 'idade': 22}]
filtrar_por_idade(pessoas, 25) deve retornar [[{'nome': 'Ana', 'idade': 25}, {'nome': 'Bruno', 'idade': 30}]'''
def filtrar_por_idade(pessoas, idade_minima):
  print('filtrar_por_idade(pessoas, idade_minima')
  #remova o print acima e escreva o código aqui
#não esqueça de chamar a função (com argumentos, se necessário) aqui abaixo!

#boa sorte
'''Dado o dicionário `produtos = {'arroz': 20, 'feijão': 10, 'macarrão': 5}`,
escreva uma função `atualizar_precos(produtos, porcentagem)` que aumente o preço de cada produto
em uma determinada porcentagem apenas se o preço atual for menor que 10.
Exemplo: atualizar_precos(produtos, 20) deve retornar {'arroz': 20, 'feijão': 10, 'macarrão': 6.0}'''
def atualizar_precos(produtos, porcentagem):
  print('atualizar_precos(produtos, porcentagem)')
  #remova o print acima e escreva o código aqui
#não esqueça de chamar a função (com argumentos, se necessário) aqui abaixo!

'''Escreva uma função `dicionario_para_tuplas(dicionario)` que receba um dicionário e retorne uma
lista de tuplas, onde cada tupla é composta por uma chave e seu valor.'''
def dicionario_para_tuplas(dicionario):
  print('dicionario_para_tuplas(dicionario)')
  #remova o print acima e escreva o código aqui
#não esqueça de chamar a função (com argumentos, se necessário) aqui abaixo!

'''
Escreva uma função `filtrar_chaves(dicionario, chaves)` que receba um dicionário e uma lista de chaves.
A função deve retornar um novo dicionário contendo apenas as chaves especificadas.
Exemplo: filtrar_chaves({'nome': 'Ana', 'idade': 25, 'curso': 'Engenharia'}, ['nome', 'curso']) deve retornar
{'nome': 'Ana', 'curso': 'Engenharia'}'''
def filtrar_chaves(dicionario, chaves):
  print('filtrar_chaves(dicionario, chaves)')
  #remova o print acima e escreva o código aqui
#não esqueça de chamar a função (com argumentos, se necessário) aqui abaixo!