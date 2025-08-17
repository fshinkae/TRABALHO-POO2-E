from datetime import date
from src.interfaces.item_interface import ItemInterface

class Item(ItemInterface):
    def __init__(self, codigo: str, titulo: str, ano: int, estoque: int = 1):
        self._codigo = codigo
        self._titulo = titulo
        self._ano = ano
        self._estoque = estoque
    
    def dias_de_emprestimo(self) -> int:
        return 14
    
    def disponivel_para_emprestimo(self) -> bool:
        return self._estoque > 0
    
    @property
    def codigo(self) -> str:
        return self._codigo
    
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def ano(self) -> int:
        return self._ano
    
    @property
    def estoque(self) -> int:
        return self._estoque
    
    @estoque.setter
    def estoque(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo")
        self._estoque = valor
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}('{self.titulo}', {self.ano})"
