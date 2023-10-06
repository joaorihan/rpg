def gerar_personagem():
    import random
    personagem = {
        "habilidade" : (random.randint(0,6) + 6),
        "sorte" : (random.randint(0,6) + 6),
        "energia" : ((random.randint(0,6) + random.randint(0,6)) + 12)
    }
    return personagem

