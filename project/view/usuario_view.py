class UsuarioView:

    def mostrar_menu(self):
        print("\n" + "═" * 50)
        print("            📋 MENU DE USUÁRIOS")
        print("═" * 50)
        print("  [1] ➜ 🆕  Criar usuário")
        print("  [2] ➜ 📄  Listar usuários")
        print("  [0] ➜ ❌  Sair")
        print("═" * 50)

    def obter_dados_usuario(self):
        print("\n" + "─" * 50)
        print("            ✏️  CADASTRO DE USUÁRIO")
        print("─" * 50)
        nome = input("👤  Nome  : ").strip()
        email = input("📧  Email : ").strip()
        print("─" * 50)
        return nome, email

    def mostrar_usuarios(self, usuarios):
        print("\n" + "═" * 60)
        print("                 👥 LISTA DE USUÁRIOS")
        print("═" * 60)

        if not usuarios:
            print("⚠️  Nenhum usuário cadastrado.")
        else:
            print(f"{'ID':<5} {'NOME':<20} {'EMAIL'}")
            print("─" * 60)
            for u in usuarios:
                print(f"{u.id:<5} {u.nome:<20} {u.email}")

        print("═" * 60)

    def mostrar_mensagem(self, mensagem):
        print("\n" + "═" * 50)
        print(f"💬  {mensagem}")
        print("═" * 50)
