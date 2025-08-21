from typing import List

class Usuario:
    """Representa um usuário da biblioteca"""
    
    def __init__(self, id_usuario: str, nome: str, limite_emprestimos: int = 3):
        self._id_usuario = id_usuario
        self._nome = nome
        self._limite_emprestimos = limite_emprestimos
        self._itens_emprestados: List['Emprestimo'] = []
    
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
    def itens_emprestados(self) -> List['Emprestimo']:
        return self._itens_emprestados
    
    def pode_emprestar(self) -> bool:
        """Verifica se o usuário pode fazer mais empréstimos"""
        return len(self._itens_emprestados) < self._limite_emprestimos
