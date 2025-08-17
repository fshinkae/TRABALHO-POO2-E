from datetime import date, timedelta
from src.interfaces.item_interface import ItemInterface
from src.models.usuario import Usuario

class Emprestimo:
    def __init__(self, item: ItemInterface, usuario: 'Usuario', data: date = None):
        self._item = item
        self._usuario = usuario
        self._data_emprestimo = data or date.today()
        self._data_devolucao = None
        self._prazo = self._data_emprestimo + timedelta(days=item.dias_de_emprestimo())
    
    @property
    def item(self) -> ItemInterface:
        return self._item
    
    @property
    def usuario(self) -> 'Usuario':
        return self._usuario
    
    @property
    def data_emprestimo(self) -> date:
        return self._data_emprestimo
    
    @property
    def data_devolucao(self) -> date:
        return self._data_devolucao
    
    @property
    def prazo(self) -> date:
        return self._prazo
    
    @property
    def em_aberto(self) -> bool:
        return self._data_devolucao is None
    
    @property
    def esta_atrasado(self) -> bool:
        if not self.em_aberto:
            return False
        return date.today() > self._prazo
    
    def devolver(self) -> None:
        if not self.em_aberto:
            raise ValueError("Empréstimo já devolvido")
        self._data_devolucao = date.today()
    
    def __str__(self) -> str:
        status = "em aberto" if self.em_aberto else f"devolvido em {self.data_devolucao}"
        return f"[{status}] {self.item} -> {self.usuario.nome} (prazo: {self.prazo})"
