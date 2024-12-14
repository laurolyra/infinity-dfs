# Aula 07: Módulos e bibliotecas em python

Olá, estudante! Neste exercício, lidaremos com uma simulação muito próxima ao dia a dia de um programador _back-end_, que é a execução de tarefas através de serviços específicos - não se preocupe por não entender muito bem esses termos agora. Posteriormente, teremos aulas específicas a respeito.

Dentro desta pasta, temos os arquivos `main.py`, `dados_pessoais.py`, `telefones.py`, `endereço.py` e `chave_pix.py`. Esses arquivos possuem funções diversas que, quando chamadas, apenas retornam uma frase do nome da função.

## Antes de começar, crie o ambiente virtual!

Crie um ambiente virtual com o número da sua turma, usando o comando `python3 -m venv [NUMERO_DA_TURMA]_aula_07`, trocando `[NUMERO_DA_TURMA]` pelo dado correspondente.

Dito isso, temos as seguintes tarefas:

1. Importe todos os módulos para o arquivo `main.py`;
2. Troque todos os `print` nas opções pela chamada das funções nos módulos importados nos arquivos - ou seja, cada opção deverá chamar uma função diferente dos módulos importados;
3. Crie uma pasta para cada módulo e coloque-o dentro dela - Nesse caso, a organização das pastas deverá ficar assim:
```
aula-07
|_chave_pix
  |_chave_pix.py
|_dados_pessoais
  |_dados_pessoais.py
# e assim por diante
```
4. Com as pastas adicionadas, refaça as importações, para que os módulos voltem a funcionar;
5. Perceba que todos os módulos possuem uma função relacionada um qr code. Refatore o seu código, dando um apelido à importação do qr code para `qr_[nome_do_arquivo_importado].py`.
6. Utilizando a biblioteca `faker`, complete as funções de criar um dado, retornando a geração de um `faker` desse dado.
7. Utilizando a biblioteca `qrcode`, [disponível aqui](https://pypi.org/project/qrcode/), complete a função `gera_qr_code` de cada módulo. fique atento que a função está esperando um argumento para que seja gerada a chave, então você pode criar um novo `input` para gerar esse código OU utilizar a biblioteca `faker` do exercício anterior.

### Desafios Maiores (boa sorte!)
1. Nossa pasta possui um arquivo chamado `banco_de_dados.json`, entenda-o como uma simulação do banco de dados. Com a ajuda da biblioteca `json`, manipule o arquivo mencionado e retorne o dicionário alterado, aplicando as operações descritas no nome da função - com um dado pessoal editado, com um endereço adicionado, etc.
2. Quer fazer um gerador de qrcode pra pix DE VERDADE? sugiro dar uma explorada na biblioteca [pixQRcode](https://github.com/Mostela/pix-qrcode). Implemente-a no projeto e tenha seu primeiro projetinho python prático!