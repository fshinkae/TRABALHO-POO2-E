from src.models.item import Item

class Livro(Item):
    def __init__(self, codigo: str, titulo: str, ano: int, autor: str, estoque: int = 1):
        super().__init__(codigo, titulo, ano, estoque)
        self._autor = autor
    
    @property
    def autor(self) -> str:
        return self._autor
    
    def dias_de_emprestimo(self) -> int:
        return 14  # Livros têm 14 dias de empréstimo
