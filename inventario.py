def gerar_mochila():
    
    mochila = { "Poção de Vida" : 5, 
                "Poção de Sorte" : 3 , 
                "espada" : 0,
                "poção da réplica": 0,
                "itens_diversos": [],
                "Peça de Ouro": 0
                }

    return mochila

def adicionar_item(mochila, loot):
    if loot in mochila:
        mochila[loot] += 1 
    else:
        mochila[loot] = 1    
    return mochila


def remover_item(mochila, item):
    if item in mochila:
        mochila[item] -= 1 
        if mochila[item] <= 0:
            mochila.pop(item)
    return mochila 
