# Refatoração do Sistema de Biblioteca

Este projeto é uma refatoração do código base de um sistema de biblioteca, aplicando os 4 pilares da Programação Orientada a Objetos.

## Histórico de Refatoração

### 1. Abstração
- Criação da classe abstrata `ItemBiblioteca`
- Definição de métodos abstratos `dias_de_emprestimo()` e `get_tipo()`
- Modelagem clara dos conceitos do domínio (Biblioteca, Usuario, Emprestimo)

### 2. Encapsulamento
- Proteção dos atributos com prefixo `_`
- Uso de `@property` para acesso controlado aos atributos
- Métodos específicos para manipulação de estado (ex: `adicionar_emprestimo()`)

### 3. Herança
- Classe base `ItemBiblioteca` com implementações específicas:
  - `Livro`: 14 dias de empréstimo
  - `Revista`: 7 dias de empréstimo
- Reutilização de código comum na classe base

### 4. Polimorfismo
- Diferentes comportamentos para `dias_de_emprestimo()`
- Implementações específicas de `get_tipo()`
- Tratamento uniforme de diferentes tipos de itens

## Como Executar
```bash
python src/main.py
```

## Estrutura do Projeto
```
src/
  ├── item.py         # Classes ItemBiblioteca, Livro, Revista
  ├── usuario.py      # Classe Usuario
  ├── emprestimo.py   # Classe Emprestimo
  ├── biblioteca.py   # Classe Biblioteca
  └── main.py         # Programa principal
```
