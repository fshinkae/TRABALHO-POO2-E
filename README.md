# Sistema de Biblioteca - Refatoração com POO

Nomes: Felipe Shinkae, Heitor Cortes, Paulo Amaral, José Guilherme, Matheus Ferreira

Este projeto demonstra a refatoração de um sistema de biblioteca aplicando os princípios da Programação Orientada a Objetos (POO).

## Pilares da POO Implementados

### 1. Encapsulamento

**Antes:**
```python
class Item:
    def __init__(self, codigo, titulo, ano, estoque=1, tipo="item"):
        self.codigo = codigo  # Acesso direto aos atributos
        self.titulo = titulo
        self.ano = ano
        self.estoque = estoque
        self.tipo = tipo
```

**Depois:**
```python
class Item(ItemInterface):
    def __init__(self, codigo: str, titulo: str, ano: int, estoque: int = 1):
        self._codigo = codigo  # Atributos privados
        self._titulo = titulo
        self._ano = ano
        self._estoque = estoque
    
    @property
    def estoque(self) -> int:  # Getter controlado
        return self._estoque
    
    @estoque.setter
    def estoque(self, valor: int) -> None:  # Setter com validação
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo")
        self._estoque = valor
```

### 2. Herança

**Antes:**
```python
class Item:
    def __init__(self, codigo, titulo, ano, estoque=1, tipo="item"):
        # Tipo definido por parâmetro
        self.tipo = tipo
```

**Depois:**
```python
class Item(ItemInterface):
    def dias_de_emprestimo(self) -> int:
        return 14

class Livro(Item):
    def __init__(self, codigo: str, titulo: str, ano: int, autor: str, estoque: int = 1):
        super().__init__(codigo, titulo, ano, estoque)
        self._autor = autor

class Revista(Item):
    def __init__(self, codigo: str, titulo: str, ano: int, edicao: str, estoque: int = 1):
        super().__init__(codigo, titulo, ano, estoque)
        self._edicao = edicao
    
    def dias_de_emprestimo(self) -> int:
        return 7  # Sobrescrita do método
```

### 3. Polimorfismo

**Antes:**
```python
# Sem polimorfismo real, usando strings para diferenciar tipos
if item.tipo == "revista":
    dias = 7
else:
    dias = 14
```

**Depois:**
```python
# Interface comum
class ItemInterface(ABC):
    @abstractmethod
    def dias_de_emprestimo(self) -> int:
        pass

# Uso polimórfico
def emprestar(self, item: ItemInterface) -> None:
    prazo = item.dias_de_emprestimo()  # Chama o método apropriado da classe
```

### 4. Abstração

**Antes:**
```python
# Sem interfaces ou abstrações claras
class Biblioteca:
    def emprestar(self, id_usuario, codigo_item):
        # Lógica misturada e acoplada
        usuario = self.buscar_usuario(id_usuario)
        item = self.buscar_item(codigo_item)
        if len(usuario.itens_emprestados) >= usuario.limite_emprestimos:
            raise PermissionError("Limite atingido")
```

**Depois:**
```python
# Interface definindo contrato
class ItemInterface(ABC):
    @abstractmethod
    def disponivel_para_emprestimo(self) -> bool:
        pass

class Usuario:
    def pode_emprestar(self) -> bool:
        return len(self._itens_emprestados) < self._limite_emprestimos

class BibliotecaService:
    def emprestar(self, id_usuario: str, codigo_item: str) -> Emprestimo:
        usuario = self.buscar_usuario(id_usuario)
        item = self.buscar_item(codigo_item)
        
        if not usuario.pode_emprestar():
            raise LimiteEmprestimosExcedidoException()
```

## Melhorias na Estrutura do Código

### 1. Organização em Módulos

**Antes:**
```
CÓDIGO BASE
└── biblioteca.py  # Todo código em um arquivo
```

**Depois:**
```
src/
├── interfaces/
│   └── item_interface.py
├── models/
│   ├── item.py
│   ├── livro.py
│   ├── revista.py
│   ├── usuario.py
│   └── emprestimo.py
├── services/
│   └── biblioteca_service.py
└── exceptions/
    └── biblioteca_exceptions.py
```

### 2. Tratamento de Exceções

**Antes:**
```python
# Exceções genéricas
raise ValueError("Código já cadastrado")
raise PermissionError("Usuário atingiu o limite")
```

**Depois:**
```python
# Hierarquia própria de exceções
class BibliotecaException(Exception):
    pass

class LimiteEmprestimosExcedidoException(BibliotecaException):
    pass

class ItemIndisponivelException(BibliotecaException):
    pass
```

### 3. Type Hints e Validações

**Antes:**
```python
def emprestar(self, id_usuario, codigo_item):
    # Sem tipagem ou validações claras
    usuario = self.usuarios[id_usuario]
```

**Depois:**
```python
def emprestar(self, id_usuario: str, codigo_item: str) -> Emprestimo:
    usuario = self.buscar_usuario(id_usuario)  # Com validação
    if not usuario.pode_emprestar():
        raise LimiteEmprestimosExcedidoException()
```

## Benefícios da Refatoração

1. **Manutenibilidade**
   - Código mais organizado e modular
   - Responsabilidades bem definidas
   - Fácil de estender e modificar

2. **Reusabilidade**
   - Classes e interfaces bem definidas
   - Componentes independentes
   - Baixo acoplamento

3. **Segurança**
   - Encapsulamento adequado
   - Validações robustas
   - Tratamento de erros específico

4. **Flexibilidade**
   - Fácil adicionar novos tipos de itens
   - Sistema extensível
   - Interfaces bem definidas

## Como Executar

```bash
# Instalar o projeto
pip install -e .

# Executar o sistema
python src/main.py
```