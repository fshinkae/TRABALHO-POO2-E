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
├── exceptions/         # Exceções personalizadas do sistema
│   └── biblioteca_exceptions.py
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

## Como Executar
```bash
python src/main.py
```

## Tratamento de Exceções 🚨

O sistema implementa um conjunto robusto de exceções personalizadas para lidar com diferentes situações de erro:

### Exceções Disponíveis

1. `ItemNaoEncontradoError`
   - Lançada quando um item não é encontrado no catálogo
   - Ex: Tentar emprestar um livro que não existe

2. `UsuarioNaoEncontradoError`
   - Lançada quando um usuário não é encontrado no sistema
   - Ex: Tentar realizar operações com um usuário inexistente

3. `ItemIndisponivelError`
   - Lançada quando um item não tem unidades disponíveis
   - Ex: Tentar emprestar um livro sem estoque

4. `LimiteEmprestimosError`
   - Lançada quando um usuário atinge seu limite de empréstimos
   - Ex: Usuário tenta pegar mais livros que seu limite permite

5. `EmprestimoNaoEncontradoError`
   - Lançada quando não é encontrado um empréstimo em aberto
   - Ex: Tentar devolver um item que não está emprestado

6. `ItemJaEmprestadoError`
   - Lançada quando um usuário tenta emprestar um item que já possui
   - Ex: Tentar emprestar o mesmo livro duas vezes

### Como as Exceções São Tratadas

```python
try:
    biblioteca.emprestar("U1", "L001")
    print("✓ Empréstimo realizado com sucesso")
except ItemIndisponivelError as e:
    print(f"✗ Erro: {e}")
except LimiteEmprestimosError as e:
    print(f"✗ Erro: {e}")
```

## Histórico de Desenvolvimento
1. ✅ Criação da estrutura base do projeto
2. ✅ Implementação da classe abstrata ItemBiblioteca
3. ✅ Desenvolvimento das classes concretas (Livro, Revista)
4. ✅ Implementação do controle de usuários
5. ✅ Sistema de empréstimos
6. ✅ Interface de usuário
7. ✅ Tratamento de exceções