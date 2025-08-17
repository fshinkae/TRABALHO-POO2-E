from src.services.biblioteca_service import BibliotecaService
from src.models.livro import Livro
from src.models.revista import Revista
from src.models.usuario import Usuario
from src.exceptions.biblioteca_exceptions import *

def criar_biblioteca_demo():
    biblioteca = BibliotecaService("Biblioteca Central")
    
    # Adicionando itens
    biblioteca.adicionar_item(
        Livro("L001", "Clean Code", 2008, "Robert C. Martin", estoque=2)
    )
    biblioteca.adicionar_item(
        Livro("L002", "Python Fluente", 2015, "Luciano Ramalho", estoque=1)
    )
    biblioteca.adicionar_item(
        Revista("R001", "Ciência Hoje", 2024, "#250", estoque=3)
    )
    
    # Cadastrando usuários
    biblioteca.cadastrar_usuario(
        Usuario("U001", "Ana Silva", "ana@email.com", limite_emprestimos=2)
    )
    biblioteca.cadastrar_usuario(
        Usuario("U002", "Bruno Santos", "bruno@email.com", limite_emprestimos=1)
    )
    
    return biblioteca

def main():
    print(">>> Biblioteca POO - Sistema de Gerenciamento")
    biblioteca = criar_biblioteca_demo()
    
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("[1] Pesquisar ITENS (por código, título ou tipo)")
        print("[2] Pesquisar USUÁRIOS (por id ou nome)")
        print("[3] Pesquisar EMPRÉSTIMOS")
        print("[4] Realizar EMPRÉSTIMO")
        print("[5] Realizar DEVOLUÇÃO")
        print("[6] Listar EMPRÉSTIMOS EM ABERTO")
        print("[7] Listar EMPRÉSTIMOS ATRASADOS")
        print("[0] Sair")
        
        op = input("\nEscolha uma opção: ").strip()
        
        try:
            if op == "0":
                print("\nAté mais!")
                break
            
            elif op == "1":
                termo = input("Termo de busca (vazio para listar todos): ").strip()
                itens = biblioteca.pesquisar_itens(termo)
                print("\nItens encontrados:")
                if not itens:
                    print("  Nenhum item encontrado.")
                for item in itens:
                    print(f"  {item.codigo}: {item} | Estoque: {item.estoque}")
            
            elif op == "2":
                termo = input("Termo de busca (vazio para listar todos): ").strip()
                usuarios = biblioteca.pesquisar_usuarios(termo)
                print("\nUsuários encontrados:")
                if not usuarios:
                    print("  Nenhum usuário encontrado.")
                for usuario in usuarios:
                    print(f"  {usuario.id_usuario}: {usuario.nome} | "
                          f"Empréstimos: {len(usuario.itens_emprestados)}/{usuario.limite_emprestimos}")
            
            elif op == "3":
                termo = input("Termo de busca (item/usuário; vazio para todos): ").strip()
                status = input("Status [enter=Todos | aberto | devolvido]: ").strip().lower() or None
                if status not in (None, "aberto", "devolvido"):
                    print("  Status inválido. Usando 'Todos'.")
                    status = None
                
                emprestimos = biblioteca.pesquisar_emprestimos(termo, status)
                print("\nEmpréstimos encontrados:")
                if not emprestimos:
                    print("  Nenhum empréstimo encontrado.")
                for emp in emprestimos:
                    print(f"  {emp}")
            
            elif op == "4":
                id_usuario = input("ID do usuário: ").strip()
                codigo_item = input("Código do item: ").strip()
                emprestimo = biblioteca.emprestar(id_usuario, codigo_item)
                print(f"\nEmpréstimo realizado com sucesso:\n  {emprestimo}")
            
            elif op == "5":
                id_usuario = input("ID do usuário: ").strip()
                codigo_item = input("Código do item: ").strip()
                biblioteca.devolver(id_usuario, codigo_item)
                print("\nDevolução realizada com sucesso!")
            
            elif op == "6":
                emprestimos = biblioteca.listar_emprestimos_em_aberto()
                print("\nEmpréstimos em aberto:")
                if not emprestimos:
                    print("  Nenhum empréstimo em aberto.")
                for emp in emprestimos:
                    print(f"  {emp}")
            
            elif op == "7":
                emprestimos = biblioteca.listar_emprestimos_atrasados()
                print("\nEmpréstimos atrasados:")
                if not emprestimos:
                    print("  Nenhum empréstimo atrasado.")
                for emp in emprestimos:
                    print(f"  {emp}")
            
            else:
                print("\nOpção inválida!")
                
        except BibliotecaException as e:
            print(f"\nErro: {str(e)}")
        except Exception as e:
            print(f"\nErro inesperado: {str(e)}")
        
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()