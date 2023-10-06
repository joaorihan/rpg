import ficha
import combate

print("Bem-Vindo")
input("Aperte Enter para começar a jogar")
jogando = True

personagem = ficha.gerar_personagem()

stats_iniciais = personagem

while jogando:
    print("Vamos gerar os Stats do seu personagem.\n")    
    ficha_formatada = ficha.ficha_formatada(personagem)

    print(ficha_formatada)
    input()

    inimigo_atual = combate.encontrou_inimigo_fraco(personagem)
print("Fim do Jogo")    
    