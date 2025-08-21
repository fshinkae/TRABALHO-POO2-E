from typing import Dict, List, Optional
from models.item import ItemBiblioteca
from models.usuario import Usuario
from models.emprestimo import Emprestimo
from exceptions.biblioteca_exceptions import (
    ItemNaoEncontradoError,
    UsuarioNaoEncontradoError,
    ItemIndisponivelError,
    LimiteEmprestimosError,
    EmprestimoNaoEncontradoError,
    ItemJaEmprestadoError
)

class Biblioteca:
    """Gerencia o catálogo de itens, usuários e empréstimos da biblioteca"""
    
    def __init__(self, nome: str):
        self._nome = nome
        self._catalogo: Dict[str, ItemBiblioteca] = {}
        self._usuarios: Dict[str, Usuario] = {}
        self._emprestimos: List[Emprestimo] = []
        
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def catalogo(self) -> Dict[str, ItemBiblioteca]:
        return self._catalogo
    
    @property
    def usuarios(self) -> Dict[str, Usuario]:
        return self._usuarios
    
    @property
    def emprestimos(self) -> List[Emprestimo]:
        return self._emprestimos
    
    def adicionar_item(self, item: ItemBiblioteca) -> None:
        """Adiciona um novo item ao catálogo"""
        if item.codigo in self._catalogo:
            raise ValueError("Código já cadastrado")
        self._catalogo[item.codigo] = item
    
    def buscar_item(self, codigo: str) -> ItemBiblioteca:
        """Busca um item pelo código"""
        if codigo not in self._catalogo:
            raise ItemNaoEncontradoError(f"Item com código '{codigo}' não encontrado")
        return self._catalogo[codigo]
    
    def cadastrar_usuario(self, usuario: Usuario) -> None:
        """Cadastra um novo usuário"""
        if usuario.id_usuario in self._usuarios:
            raise ValueError("Usuário já cadastrado")
        self._usuarios[usuario.id_usuario] = usuario
    
    def buscar_usuario(self, id_usuario: str) -> Usuario:
        """Busca um usuário pelo ID"""
        if id_usuario not in self._usuarios:
            raise UsuarioNaoEncontradoError(f"Usuário com ID '{id_usuario}' não encontrado")
        return self._usuarios[id_usuario]
    
    def emprestar(self, id_usuario: str, codigo_item: str) -> Emprestimo:
        """Realiza o empréstimo de um item para um usuário"""
        usuario = self.buscar_usuario(id_usuario)
        item = self.buscar_item(codigo_item)
        
        # Verifica se o usuário já tem este item emprestado
        for emp in self._emprestimos:
            if emp.usuario is usuario and emp.item is item and emp.em_aberto:
                raise ItemJaEmprestadoError(f"O item '{item.titulo}' já está emprestado para {usuario.nome}")
        
        if not usuario.pode_emprestar():
            raise LimiteEmprestimosError(f"Usuário {usuario.nome} atingiu o limite de empréstimos")
            
        if item.estoque <= 0:
            raise ItemIndisponivelError(f"Item '{item.titulo}' não possui unidades disponíveis")
            
        item.estoque -= 1
        emp = Emprestimo(item, usuario)
        usuario.adicionar_emprestimo(emp)
        self._emprestimos.append(emp)
        return emp
    
    def devolver(self, id_usuario: str, codigo_item: str) -> None:
        """Registra a devolução de um item"""
        usuario = self.buscar_usuario(id_usuario)
        item = self.buscar_item(codigo_item)
        
        emprestimo = next(
            (e for e in self._emprestimos 
             if e.usuario is usuario and e.item is item and e.em_aberto),
            None
        )
        
        if not emprestimo:
            raise EmprestimoNaoEncontradoError(
                f"Não foi encontrado empréstimo em aberto do item '{item.titulo}' para o usuário {usuario.nome}"
            )
            
        emprestimo.devolver()
        item.estoque += 1
        usuario.remover_emprestimo(emprestimo)
    
    def pesquisar_itens(self, termo: Optional[str] = None) -> List[ItemBiblioteca]:
        """Pesquisa itens por termo"""
        t = (termo or "").strip().lower()
        if not t:
            return list(self._catalogo.values())
            
        return [
            item for item in self._catalogo.values()
            if (t in str(item.codigo).lower() or
                t in str(item.titulo).lower() or
                t in str(item.get_tipo()).lower())
        ]
    
    def pesquisar_usuarios(self, termo: Optional[str] = None) -> List[Usuario]:
        """Pesquisa usuários por termo"""
        t = (termo or "").strip().lower()
        if not t:
            return list(self._usuarios.values())
            
        return [
            u for u in self._usuarios.values()
            if (t in str(u.id_usuario).lower() or
                t in str(u.nome).lower())
        ]
    
    def pesquisar_emprestimos(self, termo: Optional[str] = None, status: Optional[str] = None) -> List[Emprestimo]:
        """Pesquisa empréstimos por termo e status"""
        t = (termo or "").strip().lower()
        
        def casa(e: Emprestimo) -> bool:
            alvo = (
                t in str(e.item.codigo).lower() or
                t in str(e.item.titulo).lower() or
                t in str(e.usuario.id_usuario).lower() or
                t in str(e.usuario.nome).lower()
            ) if t else True
            
            if not alvo:
                return False
                
            if status == "aberto":
                return e.em_aberto
            if status == "devolvido":
                return not e.em_aberto
            return True
        
        return [e for e in self._emprestimos if casa(e)]
