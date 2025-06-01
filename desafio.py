"""
Projeto: Lista de compras

Crie um programa para gerenciar uma lista de compras que contenha o nome de cada item e a quantidade desejada. 
Implemente as seguintes funcionalidades, por meio de um menu de opções para que o usuário interaja com o sistema: 
adicionar um novo item; 
remover um item; 
atualizar quantidade de um item já existente; 
visualizar toda a lista de compras; 
sair do programa.

Dicas:
Utilize um laço de repetição para representar o menu de opções, de modo que este fique ativo até o usuário selecionar a opção “sair”;
Teste cada função separadamente antes de unificá-la no menu;
Lembre-se de verificar se um item já existe. Se isso acontecer, basta incrementar ou atualizar sua quantidade.
"""

lista_compras = {} # chave(str) = nome ; valor(int) = qtde

def adicionar_item(item: str, qtde: int) -> None:
    """
    Adiciona um item e sua quantidade desejada à lista de compras.
    Se o item já estiver na lista, a quantidade informada será somada à preexistente.
    """
    if item in lista_compras:
        print(f"(!) O item {item} já está em sua lista de compras.")
        lista_compras[item] += qtde
        
        # Implementar somente no desafio !!
        # Se o item já estiver na lista, o usuário decide por somar com a quantidade existente ou atualizar com o novo valor.
        #escolha = input("Deseja somar a quantidade ou atualizar? (0 -> soma / 1 -> atualizar): ")
        
        #if escolha == '0':  # somar
        #    lista_compras[item] += qtde
        #    print(f"A quantidade de '{item}' foi somada. Nova quantidade: {lista_compras[item]}.")
        #elif escolha == '1':  # atualizar
        #    atualizar_qtde(item, qtde)
        #else:
        #    print("(!) Opção inválida. Nenhuma alteração foi feita.")
        
    else:  # se o item não existe
        lista_compras[item] = qtde


def remover_item(item: str) -> None:
    """
    Remove um item e sua quantidade da lista de compras.
    """
    # antes de pedir pra remover direto, verificar se a lista está vazia -> não remove nada (nem pergunta), apenas informa
    if item in lista_compras:
        del lista_compras[item]
        print(f"\nO item '{item}' foi removido de sua lista de compras.")
    else:
        print(f"(!) O item '{item}' não está na lista de compras.")


def atualizar_qtde(item: str, qtde: int) -> None:
    """
    Atualize a quantidade de um item na lista de compras.
    Verificar se chegar em 0 e já remover?
    """
    # antes de atualizar direto, verificar se a lista está vazia -> não atualizada nada, apenas informa
    if item in lista_compras:
        if qtde <= 0:
            remover_item(item)
        else: # atualiza com a nova quantidade
            lista_compras[item] = qtde
            print(f"\nA quantidade do item '{item}' foi atualizada para {lista_compras[item]}.")
    else:
        print(f"\n(!) O item '{item}' não está na lista de compras.")


def visualizar_itens() -> None:
    if not lista_compras:
        print("\n(!) A lista de compras está vazia.")
    else:
        print("\n--- Lista de Compras ---")
        for item, qtde in lista_compras.items():
            print(f"- {item}: {qtde}")


def menu() -> None:
    """
    adicionar um novo item; 
    remover um item; 
    atualizar quantidade de um item já existente; 
    visualizar toda a lista de compras; 
    sair do programa.
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

        elif opcao == "3":  # Atualizar quantidade de um item
            item = input("\nNome do item a atualizar: ")
            qtde = int(input("Nova quantidade: "))
            atualizar_qtde(item, qtde)
            
        elif opcao == "4":  # Visualizar toda a lista de compras
            visualizar_itens()

        elif opcao == "5":
            print("\nSaindo do programa...")
            loop = False

        else:
            print("(!) Opção inválida. Tente novamente.")

menu()