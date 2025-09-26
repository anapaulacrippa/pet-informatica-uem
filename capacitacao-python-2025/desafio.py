"""
PET-Informática
Capacitação Lógica + Python - Dia 04
(Desafio) Projeto Prático: Carrinho de Compras
"""

carrinho_compras = {}   # chave(str) = nome ; valor(int) = qtde

def adicionar_item(item: str, qtde: int) -> None:
    """
    Adiciona um item e sua quantidade desejada ao carrinho de compras.
    Se o item já estiver no carrinho, a quantidade informada será somada à preexistente.
    """
    if item in carrinho_compras:
        print("\n(!) O item", item, "já está em seu carrinho de compras.\nSua quantidade foi somada com a pré-existente.")
        carrinho_compras[item] += qtde
    else:   # se o item não existe
        carrinho_compras[item] = qtde


def remover_item(item: str) -> None:
    """
    Remove um item e sua quantidade do carrinho de compras.
    """
    if item in carrinho_compras:
        del carrinho_compras[item]
        print("\nO item", item, "foi removido de seu carrinho de compras.")
    else:   # item não encontrado
        print("\n(!) O item", item, "não está em seu carrinho de compras.")


def atualizar_qtde() -> None:
    """
    Atualiza a quantidade de um item no carrinho de compras.
    Caso a nova quantidade seja menor ou igual a zero, o item deve ser removido.
    """
    if carrinho_compras:
        item = input("\nNome do item a atualizar: ")
        if item in carrinho_compras:
            qtde = int(input("Nova quantidade: "))
            if qtde <= 0:
                remover_item(item)
            else:   # atualiza com a nova quantidade
                carrinho_compras[item] = qtde
                print(f"\nA quantidade do item {item} foi atualizada para {carrinho_compras[item]}.")
        else:
            print("\n(!) O item", item, "não está em seu carrinho de compras. Não há nada a atualizar.")
    else:
        print("\n(!) O carrinho de compras está vazio. Não há nada a atualizar.")    


def visualizar_itens() -> None:
    """
    Mostra todos os itens do carrinho de compras, caso existam.
    """
    for item, qtde in carrinho_compras.items():
        print(f"\n- {item} : {qtde}")


def total_itens() -> int:
    """
    Calcula e mostra a quantidade total de itens no carrinho de compras.
    """
    total = 0
    for qtde in carrinho_compras.values():
        total = total + qtde
    print(f"A quantidade total de itens no seu carrinho de compras é {total}.")


def menu() -> None:
    """
    Menu de opções com o qual o usuário interage.
    """
    loop = True
    while loop:
        print("\n=== MENU - Carrinho de Compras ===")
        print("1. Adicionar um novo item")
        print("2. Remover um item")
        print("3. Atualizar quantidade de um item")
        print("4. Visualizar todo o carrinho de compras")
        print("5. Visualizar quantidade total de itens")
        print("6. Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":  # adicionar um novo item
            item = input("\nNome do item a adicionar: ")
            qtde = int(input("Quantidade a adicionar: "))
            adicionar_item(item, qtde)
            
        elif opcao == "2":  # remover um item
            if carrinho_compras:  # verifica se há itens no carrinho
                item = input("\nNome do item a remover: ")
                remover_item(item)
            else:
                print("\n(!) O carrinho de compras está vazio. Não há nada a remover.")
        elif opcao == "3":  # atualizar quantidade de um item
            atualizar_qtde()
            
        elif opcao == "4":  # visualizar todo o carrinho de compras
            if carrinho_compras:  # verifica se há itens no carrinho
                visualizar_itens()
            else:
                print("\n(!) O carrinho de compras está vazio. Não há nada a visualizar")

        elif opcao == "5":  # visualizar quantidade total de itens
            total_itens()

        elif opcao == "6":
            print("\nSaindo do programa...")
            loop = False

        else:
            print("(!) Opção inválida. Tente novamente.")

menu()