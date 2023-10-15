def encontrou_inimigo(personagem, inimigo_atual):
    import random
    import json

    inimigos = {}

    with open('./inimigos_root.json', 'r', encoding="utf-8") as arquivo:
        inimigos = json.loads(arquivo.read())

    # print(inimigo_atual)

    if inimigo_atual != "":
        print(f"Você encontrou um {inimigo_atual.lower().capitalize()}!")
        print(f'\n{inimigo_atual}\nHabilidade: {(inimigos[inimigo_atual]["habilidade"])}\nEnergia: {(inimigos[inimigo_atual]["energia"])}')
        resposta = input("\nVocê deseja Lutar ou tentar correr? (Lutar/Correr)").lower()
        if resposta in ["lutar","correr"]:
            if resposta == "correr":
                sorte = random.randint(1,6) + personagem["sorte"]
                if sorte >= 15:
                    print("\nVocê dá sorte e consegue fugir")
                    fugiu = True
                else: 
                    print("\nVocê tropeça e não consegue correr.")
                    fugiu = False
            if resposta == "lutar" or fugiu == False:
                print(f"\nVocê está lutando contra {inimigo_atual.lower().capitalize()}")
            elif fugiu == True:
                print("Continuar história...") #fazer: terminar mecânica de fugir
                return fugiu
    else:
        print("Deu erro essa porra") #fazer: handle dos erros
    return inimigo_atual    

def batalha(personagem, inimigo_atual):
    import random
    import ficha
    import json
    
    batalhando = True

    inimigos = {}

    with open('./inimigos_root.json', 'r', encoding="utf-8") as arquivo:
        inimigos = json.loads(arquivo.read())


    while batalhando:
        print("\nEscolha uma ação: (Atacar/Inventário)")
        acao = input("Digite a ação desejada: ").lower()

        if acao == "atacar" or acao == "ataque":
            dano_jogador = personagem["habilidade"] + (random.randint(1,6)+random.randint(1,6))
            dano_inimigo = (inimigos[inimigo_atual]["habilidade"] + (random.randint(1,6)+random.randint(1,6)))
            

            #Inimigo Ganha
            if dano_inimigo > dano_jogador and dano_inimigo !=0 :
                print(f"\nO ataque do seu inimigo prevaleceu, te causando {dano_inimigo - dano_jogador} de dano")
                personagem["energia"] -= (dano_inimigo - dano_jogador)
            #Player Ganha
            elif dano_jogador >= dano_inimigo:
                print("Seu ataque prevaleceu")
                print(f"\nVocê atacou o {inimigo_atual.lower().capitalize()} causando {dano_jogador - dano_inimigo + 1} de dano!")
                inimigos[inimigo_atual]["energia"] -= (dano_jogador - dano_inimigo + 1)
                

        elif acao == "inventário" or acao == "inventario" or acao == "inv":
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

        print(f'\n{inimigo_atual.lower().capitalize()}\nHabilidade: {(inimigos[inimigo_atual]["habilidade"])}\nEnergia: {(inimigos[inimigo_atual]["energia"])}')

        if inimigos[inimigo_atual]["energia"] <= 0:
            print(f"\nVocê derrotou o {inimigo_atual.lower().capitalize()}!")
            break

        if personagem["energia"] <= 0:
            print(f"\nVocê não tem mais energia e morre derrotado pelo {inimigo_atual.lower().capitalize()}!")
            morreu = True
            return morreu
                

    return personagem, inimigos
