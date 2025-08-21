from datetime import date, timedelta
from typing import Optional
from src.item import ItemBiblioteca
from src.usuario import Usuario

class Emprestimo:
    """Representa um empréstimo de um item para um usuário"""
    
    def __init__(self, item: ItemBiblioteca, usuario: Usuario, data: Optional[date] = None):
        self._item = item
        self._usuario = usuario
        self._data_emprestimo = data or date.today()
        self._data_devolucao: Optional[date] = None
        self._prazo = self._data_emprestimo + timedelta(days=item.dias_de_emprestimo())
    
    @property
    def item(self) -> ItemBiblioteca:
        return self._item
    
    @property
    def usuario(self) -> Usuario:
        return self._usuario
    
    @property
    def em_aberto(self) -> bool:
        return self._data_devolucao is None
