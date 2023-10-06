
def encontrou_inimigo_fraco(personagem):
    import random
    inimigos = {
        "ORC": {"habilidade": 7, "energia": 7},
                "Golem": {"habilidade": 5, "energia": 12}
    }

    inimigo_atual = "ORC"
    # print(inimigo_atual)

    if "ORC" in inimigo_atual:
        print("Você encontrou um Orc!")
        print(f'\nOrc\nHabilidade: {(inimigos[inimigo_atual]["habilidade"])}\nEnergia: {(inimigos[inimigo_atual]["energia"])}')
        resposta = input("\nVocê deseja Lutar ou tentar correr? (Lutar/Correr)")
        if resposta in ["lutar","correr"]:
            if resposta == "correr":
                sorte = random.randint(1,6) + personagem["sorte"]
                if sorte >= 12:
                    print("\nVocê dá sorte e consegue fugir")
                    fugiu = True
                else: 
                    print("\nVocê tropeça e não consegue correr. Lute")
                    fugiu = False
            if resposta == "lutar" or fugiu == False:
                print(f"\nVocê está lutando contra {inimigo_atual.lower().capitalize()}")
            elif fugiu == True:
                print("Continuar história...") #to-do    
                return fugiu
    else:
        print("Deu erro essa porra") #to-do 
    return inimigo_atual    

def batalha(personagem, inimigo_atual):
    import random
    import ficha
    batalhando = True

    inimigos = {
        "ORC": {"habilidade": 7, "energia": 7},
                "Golem": {"habilidade": 5, "energia": 12}
    }

    while batalhando:
        print("\nEscolha uma ação: (Atacar/Inventário)")
        acao = input("Digite a ação desejada: ").lower()

        if acao == "atacar":
            dano_jogador = personagem["habilidade"] + (random.randint(1,6)+random.randint(1,6))
            dano_inimigo = (inimigos["ORC"]["habilidade"] + (random.randint(1,6)+random.randint(1,6)))
            # print("j", dano_jogador)
            # print("i", dano_inimigo)

            #Inimigo Ganha
            if dano_inimigo > dano_jogador and dano_inimigo !=0 :
                print(f"O ataque do seu inimigo prevaleceu, te causando {dano_inimigo - dano_jogador} de dano")
                personagem["energia"] -= (dano_inimigo - dano_jogador)
            #Jogador Ganha
            if dano_jogador >= dano_inimigo:
                print(f"\nVocê atacou o {inimigo_atual.lower().capitalize()} causando {dano_jogador - dano_inimigo + 1} de dano!")
                inimigos[inimigo_atual]["energia"] -= dano_jogador
                

        elif acao == "inventário":
            print("\nEscolha um item para usar: ((1)Poção de Vida / (2)Poção de Sorte)")
            item = input("Digite o item desejado: ").lower()

            if item == "poção de vida" or item == "1":
                personagem["energia"] += 5
                print(f"\nVocê usou a Poção de Vida, recuperando 5 de energia!")

            elif item == "poção de sorte" or item == "2":
                personagem["sorte"] += 2
                print(f"\nVocê usou a Poção de Energia, recuperando 3 de energia!")

        print(f"Seus stats atuais são:")
        print(ficha.ficha_formatada(personagem))

        print(f'\nOrc\nHabilidade: {(inimigos[inimigo_atual]["habilidade"])}\nEnergia: {(inimigos[inimigo_atual]["energia"])}')

        if inimigos[inimigo_atual]["energia"] <= 0:
            print(f"\nVocê derrotou o {inimigo_atual.lower().capitalize()}!")
            break

        if personagem["energia"] <= 0:
            print(f"\nVocê não tem mais energia e morre derrotado pelo {inimigo_atual.lower().capitalize()}!")
            break

    return personagem, inimigos


# def ataques(personagem):
#     inimigos = {
#     "ORC" : {"habilidade" : 7, 
#              "energia" : 7}
#     }
#     import random
#     print("Você e seu inimigo trocam golpes.")
#     ataque_inimigo = (inimigos["ORC"]["habilidade"] + (random.randint(1,6)+random.randint(1,6)))
#     ataque_jogador = (personagem["habilidade"] + (random.randint(1,6)+random.randint(1,6)))
#     print(f"Seu ataque é {ataque_jogador}")
#     if ataque_jogador >= ataque_inimigo:
#         print(f"\n\nSeu ataque prevaleceu\nEle causa um dano de {ataque_jogador}")
#         inimigos["ORC"]["energia"] -= ataque_jogador
#        to-do