import ficha

print("Bem-Vindo")

personagem = ficha.gerar_personagem()
print(personagem["sorte"])

personagem["sorte"] -= 1

print(personagem["sorte"])

