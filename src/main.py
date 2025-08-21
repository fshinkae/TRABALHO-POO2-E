from controllers.biblioteca import Biblioteca
from models.item import Livro, Revista
from models.usuario import Usuario
from exceptions.biblioteca_exceptions import (
    ItemNaoEncontradoError,
    UsuarioNaoEncontradoError,
    ItemIndisponivelError,
    LimiteEmprestimosError,
    EmprestimoNaoEncontradoError,
    ItemJaEmprestadoError
)

def demo():
    try:
        print(">>> Biblioteca base")
        biblioteca = Biblioteca("Biblioteca Central")
        
        # Adiciona itens ao catálogo
        biblioteca.adicionar_item(Livro("L001", "Clean Code", 2008, estoque=2))
        biblioteca.adicionar_item(Livro("L002", "Python Fluente", 2015, estoque=1))
        biblioteca.adicionar_item(Revista("R001", "Ciência Hoje #250", 2024, estoque=3))
        
        # Cadastra usuários
        biblioteca.cadastrar_usuario(Usuario("U1", "Ana", limite_emprestimos=2))
        biblioteca.cadastrar_usuario(Usuario("U2", "Bruno", limite_emprestimos=1))
        
        # Realiza alguns empréstimos iniciais
        try:
            biblioteca.emprestar("U1", "L001")
            print("  ✓ Empréstimo realizado: L001 para Ana")
        except (ItemIndisponivelError, LimiteEmprestimosError, ItemJaEmprestadoError) as e:
            print(f"  ✗ Erro ao emprestar: {e}")
            
        try:
            biblioteca.emprestar("U1", "R001")
            print("  ✓ Empréstimo realizado: R001 para Ana")
        except (ItemIndisponivelError, LimiteEmprestimosError, ItemJaEmprestadoError) as e:
            print(f"  ✗ Erro ao emprestar: {e}")
            
        try:
            biblioteca.emprestar("U2", "L002")
            print("  ✓ Empréstimo realizado: L002 para Bruno")
        except (ItemIndisponivelError, LimiteEmprestimosError, ItemJaEmprestadoError) as e:
            print(f"  ✗ Erro ao emprestar: {e}")
            
        try:
            biblioteca.devolver("U1", "R001")
            print("  ✓ Devolução realizada: R001 por Ana")
        except EmprestimoNaoEncontradoError as e:
            print(f"  ✗ Erro ao devolver: {e}")
            
    except Exception as e:
        print(f"Erro ao inicializar biblioteca: {e}")
        return

    while True:
        print("\n=== PESQUISAS ===")
        print("[1] Pesquisar ITENS (por código, título ou tipo)")
        print("[2] Pesquisar USUÁRIOS (por id ou nome)")
        print("[3] Pesquisar EMPRÉSTIMOS (por item/usuário)")
        print("[0] Sair")
        op = input("Escolha: ").strip().lower()
        
        match op:
            case "0":
                print("Até mais...")
                break
            
            
            case "1":
                try:
                    termo = input("Termo (se vazio lista todos): ").strip()
                    achados = biblioteca.pesquisar_itens(termo)
                    if not achados:
                        print("  Nenhum item encontrado.")
                        continue
                    for item in achados:
                        print(f"  {item.codigo}: {item} | estoque={item.estoque}")
                except Exception as e:
                    print(f"  ✗ Erro ao pesquisar itens: {e}")
                    
            case "2":
                try:
                    termo = input("Termo (se vazio lista todos): ").strip()
                    achados = biblioteca.pesquisar_usuarios(termo)
                    if not achados:
                        print("  Nenhum usuário encontrado.")
                        continue
                    for usuario in achados:
                        print(f"  {usuario.id_usuario}: {usuario.nome} | empréstimos={len(usuario.itens_emprestados)}")
                except Exception as e:
                    print(f"  ✗ Erro ao pesquisar usuários: {e}")
                    
            case "3":
                try:
                    termo = input("Termo (item/usuário; vazio lista todos): ").strip()
                    status = input("Status [enter=Todos | aberto | devolvido]: ").strip().lower() or None
                    if status not in (None, "aberto", "devolvido"):
                        print("  Status inválido. Usando 'Todos'.")
                        status = None
                    achados = biblioteca.pesquisar_emprestimos(termo, status=status)
                    if not achados:
                        print("  Nenhum empréstimo encontrado.")
                        continue
                    for emp in achados:
                        print("  ", emp)
                except Exception as e:
                    print(f"  ✗ Erro ao pesquisar empréstimos: {e}")
                    
                    
            case _:
                print("Opção inválida.")
        

if __name__ == "__main__":
    demo()