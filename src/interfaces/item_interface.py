from abc import ABC, abstractmethod
from datetime import date

class ItemInterface(ABC):
    @abstractmethod
    def dias_de_emprestimo(self) -> int:
        pass
    
    @abstractmethod
    def disponivel_para_emprestimo(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def codigo(self) -> str:
        pass
    
    @property
    @abstractmethod
    def titulo(self) -> str:
        pass
    
    @property
    @abstractmethod
    def ano(self) -> int:
        pass
    
    @property
    @abstractmethod
    def estoque(self) -> int:
        pass
