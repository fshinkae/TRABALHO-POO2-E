from src.models.item import Item

class Revista(Item):
    def __init__(self, codigo: str, titulo: str, ano: int, edicao: str, estoque: int = 1):
        super().__init__(codigo, titulo, ano, estoque)
        self._edicao = edicao
    
    @property
    def edicao(self) -> str:
        return self._edicao
    
    def dias_de_emprestimo(self) -> int:
        return 7  # Revistas têm 7 dias de empréstimo
