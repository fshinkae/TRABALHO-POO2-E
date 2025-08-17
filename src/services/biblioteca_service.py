from typing import List, Dict, Optional
from src.interfaces.item_interface import ItemInterface
from src.models.usuario import Usuario
from src.models.emprestimo import Emprestimo
from src.exceptions.biblioteca_exceptions import *

class BibliotecaService:
    def __init__(self, nome: str):
        self._nome = nome
        self._catalogo: Dict[str, ItemInterface] = {}
        self._usuarios: Dict[str, Usuario] = {}
        self._emprestimos: List[Emprestimo] = []
    
    @property
    def nome(self) -> str:
        return self._nome
    
    def adicionar_item(self, item: ItemInterface) -> None:
        if item.codigo in self._catalogo:
            raise ValueError("Código já cadastrado")
        self._catalogo[item.codigo] = item
    
    def buscar_item(self, codigo: str) -> ItemInterface:
        if codigo not in self._catalogo:
            raise ItemNaoEncontradoException(f"Item {codigo} não encontrado")
        return self._catalogo[codigo]
    
    def cadastrar_usuario(self, usuario: Usuario) -> None:
        if usuario.id_usuario in self._usuarios:
            raise ValueError("Usuário já cadastrado")
        self._usuarios[usuario.id_usuario] = usuario
    
    def buscar_usuario(self, id_usuario: str) -> Usuario:
        if id_usuario not in self._usuarios:
            raise UsuarioNaoEncontradoException(f"Usuário {id_usuario} não encontrado")
        return self._usuarios[id_usuario]
    
    def emprestar(self, id_usuario: str, codigo_item: str) -> Emprestimo:
        usuario = self.buscar_usuario(id_usuario)
        item = self.buscar_item(codigo_item)
        
        if not usuario.pode_emprestar():
            raise LimiteEmprestimosExcedidoException(
                f"Usuário {usuario.nome} atingiu o limite de empréstimos"
            )
        
        if not item.disponivel_para_emprestimo():
            raise ItemIndisponivelException(f"Item {item.titulo} não disponível")
        
        item.estoque -= 1
        emprestimo = Emprestimo(item, usuario)
        usuario.adicionar_emprestimo(emprestimo)
        self._emprestimos.append(emprestimo)
        
        return emprestimo
    
    def devolver(self, id_usuario: str, codigo_item: str) -> None:
        usuario = self.buscar_usuario(id_usuario)
        item = self.buscar_item(codigo_item)
        
        emprestimo = next(
            (e for e in self._emprestimos 
             if e.usuario is usuario and e.item is item and e.em_aberto),
            None
        )
        
        if not emprestimo:
            raise EmprestimoNaoEncontradoException("Empréstimo em aberto não encontrado")
        
        emprestimo.devolver()
        item.estoque += 1
        usuario.remover_emprestimo(emprestimo)
    
    def pesquisar_itens(self, termo: Optional[str] = None) -> List[ItemInterface]:
        if not termo:
            return list(self._catalogo.values())
        
        termo = termo.lower()
        return [
            item for item in self._catalogo.values()
            if (termo in item.codigo.lower() or
                termo in item.titulo.lower())
        ]
    
    def pesquisar_usuarios(self, termo: Optional[str] = None) -> List[Usuario]:
        if not termo:
            return list(self._usuarios.values())
        
        termo = termo.lower()
        return [
            usuario for usuario in self._usuarios.values()
            if (termo in usuario.id_usuario.lower() or
                termo in usuario.nome.lower())
        ]
    
    def listar_emprestimos_em_aberto(self) -> List[Emprestimo]:
        return [e for e in self._emprestimos if e.em_aberto]
    
    def listar_emprestimos_atrasados(self) -> List[Emprestimo]:
        return [e for e in self._emprestimos if e.em_aberto and e.esta_atrasado]
    
    def pesquisar_emprestimos(self, termo: Optional[str] = None, status: Optional[str] = None) -> List[Emprestimo]:
        emprestimos = self._emprestimos
        
        if status == "aberto":
            emprestimos = [e for e in emprestimos if e.em_aberto]
        elif status == "devolvido":
            emprestimos = [e for e in emprestimos if not e.em_aberto]
        
        if not termo:
            return emprestimos
        
        termo = termo.lower()
        return [
            emp for emp in emprestimos
            if (termo in emp.item.codigo.lower() or
                termo in emp.item.titulo.lower() or
                termo in emp.usuario.id_usuario.lower() or
                termo in emp.usuario.nome.lower())
        ]
