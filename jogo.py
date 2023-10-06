import ficha
import combate

print("Bem-Vindo")
input("Aperte Enter para começar a jogar")
jogando = True

print("Vamos gerar os Stats do seu personagem.\n")    

personagem = ficha.gerar_personagem()
ficha_formatada = ficha.ficha_formatada(personagem)
stats_iniciais = personagem

print(ficha_formatada)

while jogando:
    input("Enter para continuar")

    inimigo_atual = combate.encontrou_inimigo_fraco(personagem)
    input("Enter para continuar")

    combate.batalha(personagem, inimigo_atual)
    
print("Fim do Jogo")    
    