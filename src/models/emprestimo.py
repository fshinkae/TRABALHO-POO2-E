from datetime import date, timedelta
from typing import Optional, TYPE_CHECKING
from models.item import ItemBiblioteca

if TYPE_CHECKING:
    from models.usuario import Usuario

class Emprestimo:
    """Representa um empréstimo de um item para um usuário"""
    
    def __init__(self, item: ItemBiblioteca, usuario: 'Usuario', data: Optional[date] = None):
        self._item = item
        self._usuario = usuario
        self._data_emprestimo = data or date.today()
        self._data_devolucao: Optional[date] = None
        self._prazo = self._data_emprestimo + timedelta(days=item.dias_de_emprestimo())
    
    @property
    def item(self) -> ItemBiblioteca:
        return self._item
    
    @property
    def usuario(self) -> 'Usuario':
        return self._usuario
    
    @property
    def data_emprestimo(self) -> date:
        return self._data_emprestimo
    
    @property
    def data_devolucao(self) -> Optional[date]:
        return self._data_devolucao
    
    @property
    def prazo(self) -> date:
        return self._prazo
    
    @property
    def em_aberto(self) -> bool:
        return self._data_devolucao is None
    
    def devolver(self) -> None:
        """Registra a devolução do item"""
        if not self.em_aberto:
            raise ValueError("Empréstimo já devolvido")
        self._data_devolucao = date.today()
    
    def __str__(self) -> str:
        status = "aberto" if self.em_aberto else f"devolvido em {self._data_devolucao}"
        return f"[{status}] {self._item} -> {self._usuario.nome} (prazo {self._prazo})"
