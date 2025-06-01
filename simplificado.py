"""
PET-Informática
Capacitação Lógica + Python - Dia 04
Projeto Prático: Lista de Compras
"""

lista_compras = {} # chave(str) = nome ; valor(int) = qtde

def adicionar_item(item: str, qtde: int) -> None:
    """
    Adiciona um item e sua quantidade desejada à lista de compras.
    Se o item já estiver na lista, a quantidade informada será somada à preexistente.
    """
    if item in lista_compras:
        print("\n(!) O item", item, "já está em sua lista de compras.\nSua quantidade foi somada com a pré-existente.")
        lista_compras[item] += qtde
    else:  # se o item não existe
        lista_compras[item] = qtde


def remover_item(item: str) -> None:
    """
    Remove um item e sua quantidade da lista de compras.
    """
    if item in lista_compras:
        del lista_compras[item]
        print("\nO item", item, "foi removido de sua lista de compras.")
    else:  # item não encontrado
        print("\n(!) O item", item, "não está em lista de compras.")


def atualizar_qtde(item: str, qtde: int) -> None:
    """
    Atualiza a quantidade de um item na lista de compras.
    """
    if item in lista_compras:
        if qtde <= 0:
            remover_item(item)
        else: # atualiza com a nova quantidade
            lista_compras[item] = qtde
            print("\nA quantidade do item", item, "foi atualizada para", lista_compras[item])
    else:
        print("\n(!) O item", item, "não está em lista de compras.")


def visualizar_itens() -> None:
    """
    Mostra todos os itens da lista de compras, caso existam.
    """
    if not lista_compras:
        print("\n(!) A lista de compras está vazia.")
    else:
        print("\n--- Lista de Compras ---")
        for item, qtde in lista_compras.items():
            print("-", item, ":", qtde)


def menu() -> None:
    """
    Menu de opções com o qual o usuário interage.
    """
    loop = True
    while loop:
        print("\n=== MENU - Lista de Compras ===")
        print("1. Adicionar um novo item")
        print("2. Remover um item")
        print("3. Atualizar quantidade de um item")
        print("4. Visualizar toda a lista de compras")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":  # adicionar um novo item
            item = input("\nNome do item a adicionar: ")
            qtde = int(input("Quantidade a adicionar: "))
            adicionar_item(item, qtde)
            
        elif opcao == "2":  # remover um item
            item = input("\nNome do item a remover: ")
            remover_item(item)

        elif opcao == "3":  # atualizar quantidade de um item
            item = input("\nNome do item a atualizar: ")
            qtde = int(input("Nova quantidade: "))
            atualizar_qtde(item, qtde)
            
        elif opcao == "4":  # visualizar toda a lista de compras
            visualizar_itens()

        elif opcao == "5":  # sair
            print("\nSaindo do programa...")
            loop = False

        else:
            print("(!) Opção inválida. Tente novamente.")

menu()