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
        # fazer verificação se deseja somar ou atualizar???

        lista_compras[item] += qtde
    else:  # se o item não existe
        lista_compras[item] = qtde


def remover_item(item: str) -> None:
    """
    Remove um item e sua quantidade da lista de compras.
    """
    _ = lista_compras.pop(item)
    print(f"(!) O item {item} foi removido de sua lista de compras.")


def atualizar_qtde() -> None:
    """
    Atualize a quantidade de um item na lista de compras.
    Verificar se chegar em 0 e já remover?
    """
    pass

def visualizar_itens() -> None:
    pass

def menu() -> None:
    """
    adicionar um novo item; 
    remover um item; 
    atualizar quantidade de um item já existente; 
    visualizar toda a lista de compras; 
    sair do programa.
    """
    pass