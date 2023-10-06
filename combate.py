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
    inimigo_atual = random.choice(inimigos)

    if inimigo_atual[0] == "ORC":
        print("Você encontrou um Orc!")
        print(f'\nOrc\nHabilidade{(inimigos["ORC"]["habilidade"])}\nEnergia{(inimigos["ORC"]["energia"])}')
        resposta = input("Você deseja Lutar ou tentar correr? (Lutar/Correr)")
        if resposta in ["lutar","correr"]:
            if resposta == "correr":
                sorte = random.randint(1,6) + personagem["sorte"]
                if sorte >= 12:
                    print("Você dá sorte e consegue fugir")
                    fugiu = True
                else: 
                    print("Você não tropeça e não consegue correr. Lute")
                    fugiu = False
            if resposta == "lutar" or fugiu == False:
                print(f"Você está lutando contra {inimigo_atual[0]}")




def ataques(personagem):
    import random
    print("Você e seu inimigo trocam golpes.")
    ataque_inimigo = (inimigos["ORC"]["habilidade"] + (random.randint(1,6)+random.randint(1,6)))
    ataque_jogador = (personagem["habilidade"] + (random.randint(1,6)+random.randint(1,6)))
    print(f"Seu ataque é {ataque_jogador}")
    if ataque_jogador >= ataque_inimigo:
        print(f"\n\nSeu ataque prevaleceu\nEle causa um dano de {ataque_jogador}")
        inimigos["ORC"]["energia"] -= ataque_jogador

    