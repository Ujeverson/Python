import random
import statistics

continua = True
def gerarfaces(facesDado):
    dados = int(input("Com quantos dados quer jogar?")) #entrada da quantidade de dados que o usuário quer jogar.
    lista = [] #lista para armazenar todos os números gerados
   
   
    for i in range(dados):
        numero = random.randint(1, facesDado)
        lista.append(numero)
        print("\n Você jogou o dado",i+1, "e a face de cima é o:", numero)
    
    #estatística dos números gerados
    print("\nA soma das faces 'para cima' é", sum(lista))
    print("\nA face com maior valor é", max(lista))
    print("\nA média dos números é", statistics.mean(lista))
    print("\nA mediana é", statistics.median(lista))
    print("\nA moda é", statistics.mode(lista))
    

while continua:
    facesDado = input("\nDigite quantas faces tem o seu dado ou digite 'parar' para guardar os dados:")
    
    if facesDado == "parar":
        continua = False
    
    else:
        facesDado = int(facesDado)
        gerarfaces(facesDado)
       

print("Agora você guardou os dados!")