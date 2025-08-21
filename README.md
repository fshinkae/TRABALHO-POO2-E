# Sistema de Biblioteca - Aplicando POO

Este projeto é uma refatoração de um sistema de biblioteca demonstrando os 4 pilares da Programação Orientada a Objetos (POO).

## Estrutura do Projeto

```
src/
├── models/              # Classes que representam as entidades do sistema
│   ├── item.py         # ItemBiblioteca (abstrata), Livro e Revista
│   ├── usuario.py      # Classe Usuario
│   └── emprestimo.py   # Classe Emprestimo
├── controllers/         # Classes que controlam a lógica do sistema
│   └── biblioteca.py   # Classe Biblioteca (controle principal)
└── main.py             # Interface com usuário
```

## Os 4 Pilares da POO Explicados

### 1. Abstração 🎯
**O que é?** Simplificar conceitos do mundo real em classes.

**Como foi aplicado:**
- Classe abstrata `ItemBiblioteca` define o modelo básico de um item
- Métodos abstratos definem comportamentos obrigatórios
- Cada classe representa um conceito do mundo real (Livro, Revista, Usuario)

```python
class ItemBiblioteca(ABC):
    @abstractmethod
    def dias_de_emprestimo(self) -> int:
        pass
```

### 2. Encapsulamento 🔒
**O que é?** Proteger os dados internos da classe.

**Como foi aplicado:**
- Atributos protegidos com `_` (ex: `_nome`, `_usuarios`)
- Uso de `@property` para acesso controlado
- Métodos específicos para manipular dados

```python
class Usuario:
    def __init__(self, nome: str):
        self._nome = nome
    
    @property
    def nome(self) -> str:
        return self._nome
```

### 3. Herança 👨‍👦
**O que é?** Criar novas classes baseadas em classes existentes.

**Como foi aplicado:**
- `Livro` e `Revista` herdam de `ItemBiblioteca`
- Compartilham atributos comuns (código, título, ano)
- Cada subclasse implementa seus comportamentos específicos

```python
class Livro(ItemBiblioteca):
    def dias_de_emprestimo(self) -> int:
        return 14  # Específico para livros
```

### 4. Polimorfismo 🔄
**O que é?** Tratar diferentes classes de forma uniforme.

**Como foi aplicado:**
- Diferentes implementações de `dias_de_emprestimo()`
- Sistema trata qualquer `ItemBiblioteca` da mesma forma
- Cada tipo de item pode ter comportamento próprio

```python
# Funciona para qualquer ItemBiblioteca
def emprestar(item: ItemBiblioteca):
    prazo = item.dias_de_emprestimo()  # Polimorfismo em ação
```

## Funcionalidades

1. **Gestão de Itens**
   - Cadastro de livros e revistas
   - Controle de estoque
   - Pesquisa por código/título/tipo

2. **Gestão de Usuários**
   - Cadastro de usuários
   - Limite de empréstimos
   - Pesquisa por ID/nome

3. **Gestão de Empréstimos**
   - Realização de empréstimos
   - Devoluções
   - Pesquisa por status/item/usuário

## Como Executar
```bash
python src/main.py
```

## Histórico de Desenvolvimento
1. ✅ Criação da estrutura base do projeto
2. ✅ Implementação da classe abstrata ItemBiblioteca
3. ✅ Desenvolvimento das classes concretas (Livro, Revista)
4. ✅ Implementação do controle de usuários
5. ✅ Sistema de empréstimos
6. ✅ Interface de usuário