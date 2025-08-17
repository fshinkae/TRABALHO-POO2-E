from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.emprestimo import Emprestimo

class Usuario:
    def __init__(self, id_usuario: str, nome: str, email: str, limite_emprestimos: int = 3):
        self._id_usuario = id_usuario
        self._nome = nome
        self._email = email
        self._limite_emprestimos = limite_emprestimos
        self._itens_emprestados: List['Emprestimo'] = []
    
    @property
    def id_usuario(self) -> str:
        return self._id_usuario
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def limite_emprestimos(self) -> int:
        return self._limite_emprestimos
    
    @property
    def itens_emprestados(self) -> List['Emprestimo']:
        return self._itens_emprestados.copy()
    
    def pode_emprestar(self) -> bool:
        return len(self._itens_emprestados) < self._limite_emprestimos
    
    def adicionar_emprestimo(self, emprestimo: 'Emprestimo') -> None:
        if not self.pode_emprestar():
            raise ValueError("Limite de empréstimos atingido")
        self._itens_emprestados.append(emprestimo)
    
    def remover_emprestimo(self, emprestimo: 'Emprestimo') -> None:
        self._itens_emprestados.remove(emprestimo)
    
    def __str__(self) -> str:
        return f"{self.nome} (ID: {self.id_usuario})"