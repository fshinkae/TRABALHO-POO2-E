# Sistema de Biblioteca - Aprendendo POO na Prática

Este projeto é uma refatoração de um sistema de biblioteca para demonstrar os conceitos fundamentais da Programação Orientada a Objetos (POO). Vamos entender como cada conceito foi aplicado de forma prática!

## O que é POO?

Programação Orientada a Objetos é uma forma de organizar o código pensando em "objetos" do mundo real. Por exemplo, em uma biblioteca temos livros, revistas, usuários e empréstimos. Cada um desses é um objeto com suas próprias características e comportamentos.

## Os 4 Pilares da POO Explicados

### 1. Abstração 🎯
**O que é?** É como criar um "modelo" simplificado de algo do mundo real no código.

**Exemplo Prático:**
- Criamos uma classe `ItemBiblioteca` que representa qualquer item que pode ser emprestado
- Definimos as características básicas: código, título, ano e estoque
- É como criar uma "forma de bolo" que define o formato básico, mas não é o bolo em si!

```python
class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano, estoque):
        self.codigo = codigo
        self.titulo = titulo
        self.ano = ano
        self.estoque = estoque
```

### 2. Encapsulamento 🔒
**O que é?** É como criar uma "caixa preta" que protege as informações internas do objeto.

**Exemplo Prático:**
- Protegemos os dados dos usuários usando `_` antes do nome das variáveis
- Criamos métodos específicos para acessar e modificar esses dados
- É como um cofre: você só pode mexer no dinheiro usando os métodos certos!

```python
class Usuario:
    def __init__(self, nome):
        self._nome = nome  # Protegido
    
    @property
    def nome(self):  # Método para acessar o nome
        return self._nome
```

### 3. Herança 👨‍👦
**O que é?** É como criar "versões especializadas" de uma classe base.

**Exemplo Prático:**
- Criamos `Livro` e `Revista` que herdam de `ItemBiblioteca`
- Cada um tem suas próprias regras de empréstimo
- É como dizer que tanto livro quanto revista são itens de biblioteca, mas com algumas diferenças!

```python
class Livro(ItemBiblioteca):
    def dias_de_emprestimo(self):
        return 14  # Livros podem ser emprestados por 14 dias

class Revista(ItemBiblioteca):
    def dias_de_emprestimo(self):
        return 7   # Revistas apenas 7 dias
```

### 4. Polimorfismo 🔄
**O que é?** É a capacidade de tratar diferentes tipos de objetos de forma uniforme.

**Exemplo Prático:**
- Podemos emprestar qualquer tipo de item (livro ou revista) da mesma forma
- Cada tipo de item sabe quanto tempo pode ser emprestado
- É como ter um controle remoto universal que funciona em diferentes TVs!

```python
# Funciona tanto para livros quanto para revistas
def emprestar(item):
    prazo = item.dias_de_emprestimo()  # Cada item sabe seu prazo
    print(f"Emprestado por {prazo} dias")
```

## Como o Sistema Funciona

1. **Cadastro de Itens:**
   - Podemos adicionar livros e revistas
   - Cada um tem seu próprio prazo de empréstimo

2. **Cadastro de Usuários:**
   - Cada usuário tem um limite de empréstimos
   - Sistema controla quantos itens foram emprestados

3. **Empréstimos:**
   - Verifica se o usuário pode pegar emprestado
   - Controla os prazos automaticamente
   - Permite devoluções

## Como Executar
```bash
python src/main.py
```

## Estrutura do Projeto
```
src/
  ├── item.py         # Define ItemBiblioteca, Livro e Revista
  ├── usuario.py      # Define a classe Usuario
  ├── emprestimo.py   # Controla os empréstimos
  ├── biblioteca.py   # Gerencia todo o sistema
  └── main.py         # Interface com o usuário
```

## Histórico de Desenvolvimento
1. ✅ Criação da estrutura base do projeto
2. ✅ Implementação das classes abstratas
3. ✅ Adição do encapsulamento para proteção dos dados
4. ✅ Criação da hierarquia de itens (herança)
5. ✅ Implementação do tratamento polimórfico
6. ✅ Adição da interface de usuário