'''
Aqui é pra você treinar a importação de arquivos.
Quando este arquivo for executado, para cada opção digitada, deve-se chamar
a função que está no seu comentário.

Você não precisa necessariamente resolver os exercícios lá nos arquivos pra importar e chamar as funções aqui.
'''
opcao = int(input("selecione uma opção: "))
def menu_principal():
    if opcao == 1:
        print('opção 1')
        #chame a função retorna_0_a_5() do arquivo exercicios_de_listas.py
    if opcao == 2:
        print("opcao 2")
        #chame a função le_o_nome({'nome': 'João', 'idade': 20, 'curso': 'Engenharia'}) do arquivo exercicios_de_dicionarios.py
    if opcao == 3:
        print("opcao 3")
        #chame a função contar_unicos([1, 1, 3, 5, 5, 5, 6, 2, 18]) do arquivo exercicios_conjuntos_tuplas.py
    if opcao == 4:
        print("opcao 4")
        #chame a função tuplas_para_dicionario([('nome', 'Ana'), ('idade', 25)]) do arquivo exercicios_tudo_em_um.py

menu_principal()