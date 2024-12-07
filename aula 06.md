https://dontpad.com/dfs-710b-06

pular linha no python: \n

1. criar arquivo aula06

2. criar ambiente virtual
python3 -m venv projeto_funcoes

3. ativar o ambiente virtual:
source projeto_funcoes/bin/activate
'''
Desenvolver um programa de linha de comando que permite
aos usuários gerenciar suas tarefas diárias, atribuindo-lhes
prioridades e categorias.
'''
```python
print('lista de tarefas')

print('opções:\n1- adicionar tarefa;\n2- listar tarefa;\n3- marcar como concluída\n0- sair')
def marcar_como_concluida(troco):
    #imprimir as tarefas
    print('as tarefas são as seguintes:')
    for item in troco:
        for tupla in item.items():
            print(tupla[0] + ' da tarefa: ' + tupla[1])
    #perguntar pro usuario qual tarefa ele quer marcar
    selecionar_tarefa_para_concluir = input('insira o nome da tarefa para concluir ')
    #apos a selecao, adicionar uma chave nova pra aquela tarefa
    for item in troco:
        if item["nome"] == selecionar_tarefa_para_concluir:
            item["concluida"] = True
    menu_principal()

def imprimir_tarefas(trem):
    print(trem)
    menu_principal()

lista_de_tarefas = []

def adicionar_tarefa():
    tarefa = {}
    tarefa["nome"] = input("digite o nome da tarefa: ")
    tarefa["prioridade"] = input("qual é a prioridade? ")
    tarefa["categoria"] = input('defina a categoria: ')
    lista_de_tarefas.append(tarefa)
    menu_principal()

def menu_principal():
    menu = int(input('Selecione uma opção:'))
    if menu == 1:
        adicionar_tarefa()
    elif menu == 2:
        imprimir_tarefas(lista_de_tarefas)
    elif menu == 3:
        marcar_como_concluida(lista_de_tarefas)
    elif menu == 0:
        print('XAUBRIGADO')
        exit()

menu_principal()
```

### 1- criar nova funcionalidade para REMOVER uma tarefa pelo nome
### 2- perguntar pro usuário QUANTAS tarefas ele quer adicionar e chamar a função adicionar_tarefa quantas vezes o usuário definir
### 3- permitir que o usuário escolha se ele quer remover uma tarefa pelo nome ou por uma da(s) categoria(s)
### BOA SORTE - ao invés de "categoria", permita o usuário a inserir CATEGORIAS
