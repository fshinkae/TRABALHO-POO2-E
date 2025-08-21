from typing import List
from models.emprestimo import Emprestimo

class Usuario:
    """Representa um usuário da biblioteca"""
    
    def __init__(self, id_usuario: str, nome: str, limite_emprestimos: int = 3):
        self._id_usuario = id_usuario
        self._nome = nome
        self._limite_emprestimos = limite_emprestimos
        self._itens_emprestados: List[Emprestimo] = []
    
    @property
    def id_usuario(self) -> str:
        return self._id_usuario
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def limite_emprestimos(self) -> int:
        return self._limite_emprestimos
    
    @property
    def itens_emprestados(self) -> List[Emprestimo]:
        return self._itens_emprestados
    
    def pode_emprestar(self) -> bool:
        """Verifica se o usuário pode fazer mais empréstimos"""
        return len(self._itens_emprestados) < self._limite_emprestimos
    
    def adicionar_emprestimo(self, emprestimo: Emprestimo) -> None:
        """Adiciona um novo empréstimo à lista de empréstimos do usuário"""
        if not self.pode_emprestar():
            raise ValueError("Usuário atingiu o limite de empréstimos")
        self._itens_emprestados.append(emprestimo)
    
    def remover_emprestimo(self, emprestimo: Emprestimo) -> None:
        """Remove um empréstimo da lista de empréstimos do usuário"""
        if emprestimo in self._itens_emprestados:
            self._itens_emprestados.remove(emprestimo)
