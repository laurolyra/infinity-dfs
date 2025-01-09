'''
1- Dado o dicionário abaixo, complete a função le_o_nome,
de forma que ela retorne o valor associado à chave 'nome'.
'''
aluno = {'nome': 'João', 'idade': 20, 'curso': 'Engenharia'}
def le_o_nome():
  print('le_o_nome')
  #remova o print acima e escreva o código aqui
#não esqueça de chamar a função (com argumentos, se necessário) aqui abaixo!

'''
2- Crie um dicionário vazio chamado carro. Adicione os seguintes pares chave-valor:
'marca': 'Toyota'
'modelo': 'Corolla'
'ano': 2021
'''
#escreva o código aqui
'''
3- Remova a chave 'idade' do dicionário abaixo e imprima o dicionário atualizado.
'''
aluna = {'nome': 'Ana', 'idade': 22, 'curso': 'Medicina'}
#escreva o código aqui

'''
4- Escreva um loop for que percorra o dicionário abaixo e imprima cada chave
e seu valor correspondente no formato "Fruta: [chave], Quantidade: [valor]".
'''
frutas = {'maçã': 3, 'banana': 5, 'laranja': 2}
#escreva o código aqui
'''
5- Complete a função abaixo, que deverá receber um dicionário e uma string e, ao final, deverá retornar True ou False caso a 
chave exista ou não
Exemplo: a função verificar_chave({'rg': 12345, 'nome_da_mae': 'Luzia'}, 'nome_do_pai') deverá retornar False
'''
def verificar_chave(dicionario, chave):
  print('verificar_chave(dicionario, chave)')
  #remova o print acima e escreva o código aqui
#não esqueça de chamar a função (com argumentos, se necessário) aqui abaixo!
'''
6- Complete a função abaixo, que retorne um novo dicionário contendo apenas
os pares cujo valor seja maior ou igual a valor_minimo.
Exemplo: a função filtrar_dicionario({'a': 10, 'b': 15, 'c': 5, 'd': 20}, 10)
deve retornar {'a': 10, 'b': 15, 'd': 20}
'''
def filtrar_dicionario(dicionario, valor_minimo):
  print('filtrar_dicionario(dicionario, valor_minimo)')
  #remova o print acima e escreva o código aqui
#não esqueça de chamar a função (com argumentos, se necessário) aqui abaixo!
'''
7- Escreva uma função agrupar_por_paridade(lista) que receba uma lista de inteiros e retorne um dicionário
com duas chaves: 'pares' e 'ímpares', contendo listas de números pares e ímpares, respectivamente.
Exemplo: a função agrupar_por_paridade([1, 2, 3, 4, 5, 6, 7, 8]) deve retornar {'pares': [2, 4, 6, 8], 'ímpares': [1, 3, 5, 7]}
'''
def agrupar_por_paridade(lista):
  print('agrupar_por_paridade(lista)')
  #remova o print acima e escreva o código aqui
#não esqueça de chamar a função (com argumentos, se necessário) aqui abaixo!

#boa sorte
'''
Complete a função abaixo que deverá receber uma string frase e retornar um dicionário com a contagem de cada palavra na frase. 
Exemplo: contar_palavras("o rato roeu a roupa do rei de roma") deve retornar
{'o': 2, 'rato': 1, 'roeu': 1, 'a': 1, 'roupa': 1, 'do': 1, 'rei': 1, 'de': 1, 'roma': 1}.
'''
def contar_palavras(frase):
  print("contar_palavras(frase)")
  #remova o print acima e escreva o código aqui
#não esqueça de chamar a função (com argumentos, se necessário) aqui abaixo!