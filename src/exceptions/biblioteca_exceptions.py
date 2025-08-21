class BibliotecaException(Exception):
    """Exceção base para todas as exceções da biblioteca"""
    pass

class ItemNaoEncontradoError(BibliotecaException):
    """Exceção lançada quando um item não é encontrado no catálogo"""
    pass

class UsuarioNaoEncontradoError(BibliotecaException):
    """Exceção lançada quando um usuário não é encontrado no sistema"""
    pass

class ItemIndisponivelError(BibliotecaException):
    """Exceção lançada quando um item não está disponível para empréstimo"""
    pass

class LimiteEmprestimosError(BibliotecaException):
    """Exceção lançada quando um usuário atinge seu limite de empréstimos"""
    pass

class EmprestimoNaoEncontradoError(BibliotecaException):
    """Exceção lançada quando um empréstimo não é encontrado"""
    pass

class ItemJaEmprestadoError(BibliotecaException):
    """Exceção lançada quando um item já está emprestado para o usuário"""
    pass
