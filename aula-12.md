# Lista de Exercícios: Encapsulamento e Associação em Python

---

## **Grupo 1: Conceitos Básicos de Encapsulamento**

1. **Questão 1**: Crie uma classe `Pessoa` com atributos privados `__nome` e `__idade`. Implemente métodos públicos para definir e obter esses atributos.
2. **Questão 2**: Na classe `Pessoa`, adicione um método `aniversario()` que incrementa a idade em 1 ano.
3. **Questão 3**: Crie uma classe `ContaBancaria` com atributos privados `__saldo` e `__titular`. Implemente métodos para depositar e sacar dinheiro, garantindo que o saldo não fique negativo.
4. **Questão 4**: Na classe `ContaBancaria`, adicione um método `extrato()` que exibe o saldo atual.
5. **Questão 5**: Crie uma classe `Carro` com atributos privados `__marca`, `__modelo` e `__ano`. Implemente métodos para acessar e modificar esses atributos.

---

## **Grupo 2: Associação Simples**

6. **Questão 6**: Crie uma classe `Pedido` que associa um `Cliente` (da questão anterior) a uma lista de `Produtos`. Adicione métodos para adicionar produtos e calcular o total do pedido.
7. **Questão 7**: Na classe `Pedido`, adicione um método `listar_produtos()` que exibe todos os produtos do pedido.
8. **Questão 8**: Crie uma classe `Biblioteca` que associa `Livros` a `Usuarios`. Implemente métodos para emprestar e devolver livros.
9. **Questão 9**: Na classe `Biblioteca`, adicione um método `listar_livros_emprestados()` que exibe todos os livros emprestados por um usuário.
10. **Questão 10**: Crie uma classe `Turma` que associa `Alunos` a um `Professor`. Implemente métodos para adicionar alunos e listar todos os alunos da turma.

---

## **Grupo 3: Encapsulamento Avançado**

11. **Questão 11**: Na classe `ContaBancaria`, adicione um atributo privado `__limite` e um método para definir o limite. Garanta que o saque não ultrapasse o saldo + limite.
12. **Questão 12**: Crie uma classe `Cofre` com um atributo privado `__segredo` que só pode ser acessado por um método `abrir_cofre(senha)`.
13. **Questão 13**: Na classe `Carro`, adicione um atributo privado `__quilometragem` que só pode ser modificado por um método `rodar(km)`.
14. **Questão 14**: Crie uma classe `CaixaEletronico` que encapsula operações como `consultar_saldo()`, `depositar()` e `sacar()`, garantindo que o saldo não fique negativo.
15. **Questão 15**: Na classe `Pessoa`, adicione um atributo privado `__cpf` que só pode ser acessado por um método `verificar_cpf()`.

---

## **Grupo 4: Associação Complexa**

16. **Questão 16**: Crie uma classe `Escola` que associa `Turmas` a `Professores` e `Alunos`. Implemente métodos para adicionar turmas, professores e alunos, e listar todas as turmas de um professor.
17. **Questão 17**: Na classe `Escola`, adicione um método `listar_alunos_por_turma()` que exibe todos os alunos de uma turma específica.
18. **Questão 18**: Crie uma classe `Loja` que associa `Produtos` a `Clientes` e `Vendedores`. Implemente métodos para registrar vendas e listar todas as vendas de um vendedor.
19. **Questão 19**: Na classe `Loja`, adicione um método `calcular_total_vendas()` que retorna o valor total de todas as vendas.
20. **Questão 20**: Crie uma classe `RedeSocial` que associa `Usuarios` a `Amigos` e `Postagens`. Implemente métodos para adicionar amigos, postar mensagens e listar todas as postagens de um usuário.
