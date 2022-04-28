import random

continua = True
def gerarfaces(facesDado):
    dados = int(input("Com quantos dados quer jogar?")) #entrada da quantidade de dados que o usuário quer jogar.
    for i in range(dados):
        numero = random.randint(1, facesDado)
        print("\n Você jogou o dado",i+1, "e a face de cima é o:", numero)

while continua:
    facesDado = input("\nDigite quantas faces tem o seu dado ou digite 'parar' para guardar os dados:")
    
    if facesDado == "parar":
        continua = False
    
    else:
        facesDado = int(facesDado)
        gerarfaces(facesDado)
       

print("Agora você guardou os dados!")