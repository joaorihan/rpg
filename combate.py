inimigos = {
    "ORC" : {"habilidade" : 7, 
             "energia" : 7
            #  , 
            #  "ataque" : inimigos["ORC"]["habilidade"] + (random.randint(0,6)+random.randint(0,6))
             }, 
   
   "Golem de Gelo" : {"habilidade" : 6, 
                       "energia" : 12
                    #    ,
                    #    "ataque" : inimigos["ORC"]["habilidade"] + (random.randint(0,6)+random.randint(0,6))
                       }
    }

def encontrou_inimigo_fraco(personagem):
    import random
    
    # ataque_jogador = (personagem["habilidade"] + (random.randint(0,6)+random.randint(0,6)))

    if random.randint(0,1) == 0:
        print("Você encontrou um Orc!")
        print(f'\nOrc\nHabilidade{(inimigos["ORC"]["habilidade"])}\nEnergia{(inimigos["ORC"]["energia"])}')


def ataques(personagem):
    import random
    print("Você e seu inimigo trocam golpes.")
    ataque_inimigo = (inimigos["ORC"]["habilidade"] + (random.randint(0,6)+random.randint(0,6)))
    ataque_jogador = (personagem["habilidade"] + (random.randint(0,6)+random.randint(0,6)))
    print(f"Seu ataque é {ataque_jogador}")
    if ataque_jogador >= ataque_inimigo:
        print(f"\n\nSeu ataque prevaleceu\nEle causa um dano de {ataque_jogador}")
        inimigos["ORC"]["energia"] -= ataque_jogador

    