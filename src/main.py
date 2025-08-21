from src.controllers.biblioteca import Biblioteca
from src.models.item import Livro, Revista
from src.models.usuario import Usuario

def demo():
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
    biblioteca.emprestar("U1", "L001")
    biblioteca.emprestar("U1", "R001")
    biblioteca.emprestar("U2", "L002")
    biblioteca.devolver("U1", "R001")

    while True:
        print("\n=== PESQUISAS ===")
        print("[1] Pesquisar ITENS (por código, título ou tipo)")
        print("[2] Pesquisar USUÁRIOS (por id ou nome)")
        print("[3] Pesquisar EMPRÉSTIMOS (por item/usuário)")
        print("[0] Sair")
        op = input("Escolha: ").strip().lower()

        if op == "0":
            print("Até mais...")
            break

        if op == "1":
            termo = input("Termo (se vazio lista todos): ").strip()
            achados = biblioteca.pesquisar_itens(termo)
            if not achados:
                print("  Nenhum item encontrado.")
            else:
                for item in achados:
                    print(f"  {item.codigo}: {item} | estoque={item.estoque}")

        elif op == "2":
            termo = input("Termo (se vazio lista todos): ").strip()
            achados = biblioteca.pesquisar_usuarios(termo)
            if not achados:
                print("  Nenhum usuário encontrado.")
            else:
                for usuario in achados:
                    print(f"  {usuario.id_usuario}: {usuario.nome} | empréstimos={len(usuario.itens_emprestados)}")

        elif op == "3":
            termo = input("Termo (item/usuário; vazio lista todos): ").strip()
            status = input("Status [enter=Todos | aberto | devolvido]: ").strip().lower() or None
            if status not in (None, "aberto", "devolvido"):
                print("  Status inválido. Usando 'Todos'.")
                status = None
            achados = biblioteca.pesquisar_emprestimos(termo, status=status)
            if not achados:
                print("  Nenhum empréstimo encontrado.")
            else:
                for emp in achados:
                    print("  ", emp)
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    demo()