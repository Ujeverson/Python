import random

continua = True

while continua:
    facesDado = input("Digite quantas faces tem o seu dado ou digite 'parar' para guardar os dados:")
    
    if facesDado == "parar":
        continue = False
    
    else:
        facesDado = int(facesDado)
        dados = int(input("Com quantos dados quer jogar?")) #entrada da quantidade de dados que o usuário quer jogar.
        for i in range(dados):
            numero = random.randint(1, facesDado)
            print("Você jogou o dado e a face de cima é o:", numero)

print("Você guardou os dados!")