def adicionar_contato(contatos, nome_contato="", telefone_contato="", email_contato=""):
    contato =  {"Nome": nome_contato, "Telefone": telefone_contato, "Email": email_contato, "Favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionado.")
    return

def visualizar_contato(contatos):
   print("\n Lista de Contatos:")
   for indice, contato in enumerate(contatos, start=1):
       status = "💖" if contato["Favorito"] else " "
       nome_contato = contato["Nome"]
       email_contato = contato["Email"]
       telefone_contato = contato["Telefone"]
       print(f"{indice}. [{status}] nome: {nome_contato}, email: {email_contato}, telefone: {telefone_contato}")
   return


def editar_contato(contatos, indice_contato, nome_contato_atualizado, email_contato_atualizado, telefone_contato_atualizado):
    print("\n Editar Contato")
    print(telefone_contato_atualizado, email_contato_atualizado)
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len (contatos):
        if len(nome_contato_atualizado) > 0:
            contatos[indice_contato_ajustado]["Nome"] = nome_contato_atualizado
        if len(email_contato_atualizado) > 0:
            contatos[indice_contato_ajustado]["Email"] = email_contato_atualizado
        if len(telefone_contato_atualizado) > 0:
            contatos[indice_contato_ajustado]["Telefone"] = telefone_contato_atualizado
        print(f"\nContato {indice_contato} atualizado")
    else:
        print("Índice de contato inválido.")
    return

contatos = []
while True:
    print("\nGerenciador de Lista de contatos:")
    print("1. Adicionar Contatos")
    print("2. Ver Contatos")
    print("3. Atualizar Contatos")
    print("4. Favoritar Contatos")
    print("5. Deletar Contatos")
    print("6. Sair")

    escolha = input("\nDigite a sua escolha:")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato que quer adicionar:")
        telefone_contato = input("Digite o telefone do contato: ")
        email_contato = input("Digite o email do contato: ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    elif escolha == "2":
        visualizar_contato(contatos)
    elif escolha == "3":
        visualizar_contato(contatos)
        indice_contato = input("O digite o numero da Lista de contato que deseja atualizar: ")
        nome_contato_atualizado = input("Digite o nome do contato atual do contato ou dar Enter: ")
        telefone_contato_atualizado = input("Digite o telefone atual do contato ou dar Enter: ")
        email_contato_atualizado = input("Digite o email atual do contato ou dar Enter: ")
        editar_contato(contatos, indice_contato, nome_contato_atualizado, email_contato_atualizado, telefone_contato_atualizado)
        visualizar_contato(contatos)
    else:
       print("Encerrado")