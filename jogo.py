import ficha
import combate

print("Bem-Vindo")
input("Aperte Enter para começar a jogar")
jogando = True

personagem = ficha.gerar_personagem()

while jogando:
    print("Vamos gerar os Stats do seu personagem.\n")    
    ficha_formatada = ficha.ficha_formatada(personagem)

    print(ficha_formatada)
    input()

print("Fim do Jogo")    
    