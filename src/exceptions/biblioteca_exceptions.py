class BibliotecaException(Exception):
    """Exceção base para todas as exceções da biblioteca"""
    pass

class ItemNaoEncontradoException(BibliotecaException):
    """Exceção lançada quando um item não é encontrado"""
    pass

class UsuarioNaoEncontradoException(BibliotecaException):
    """Exceção lançada quando um usuário não é encontrado"""
    pass

class LimiteEmprestimosExcedidoException(BibliotecaException):
    """Exceção lançada quando o usuário atinge o limite de empréstimos"""
    pass

class ItemIndisponivelException(BibliotecaException):
    """Exceção lançada quando não há estoque disponível do item"""
    pass

class EmprestimoNaoEncontradoException(BibliotecaException):
    """Exceção lançada quando um empréstimo não é encontrado"""
    pass
