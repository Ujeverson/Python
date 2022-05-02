#Criar um robo que se movimenta em uma matriz 10 x 10

import random
#Criar um robo que se movimenta em uma matriz 10 x 10
class Localizacao(object):
    def __init__(self, x, y): 
        self.x = x 
        self.y = y
    
    def __str__(self):
        return '<%s, %s>' % (self.x, self.y)
class Gift(Localizacao):
    def __init__(self, x, y, name): 
        super(Gift, self).__init__(x,y)
        self.name = name
    
    def __str__(self):
        return '<%s, %s>: %s' % (self.x, self.y,self.name)
    
    def __repr__(self):
        return '<Gift> %s' % str(self)

class Robo(Localizacao):
        
    def mover_cima(self): #ou mover p cima
        
        if self.y < 10:
            self.y = self.y + 1
        else:
            print("O espaço acabou!")
        
    
    def mover_baixo(self):
       
        if self.y > 0:
            self.y = self.y - 1
        else:
            print("O espaço acabou!")
            
    def mover_esquerda(self):
       
        if self.x > 0:
            self.x = self.x - 1
        else:
            print("O espaço acabou!")
            
    def mover_direita(self):
      
        if self.x < 10:
            self.x = self.x + 1
        else:
            print("O espaço acabou!")

#verifica se o robo encontrou o "presente"
def check_gift(robo, gifts):
    ok = False
    for gift in gifts:
        if gift.x == robo.x and gift.y == robo.y:
            print("O robo encontrou o gift:", gift.name)
            ok = True
            
    return ok

#criar gifts no "mapa"
g1 = Gift(random.randint(0,10), random.randint(0,10), 'energia')
g2 = Gift(random.randint(0,10), random.randint(0,10), 'lubrificante')
g3 = Gift(random.randint(0,10), random.randint(0,10), 'arma')

gifts = [g1, g2, g3]

#Ver onde estão os gifts naquele momento
gifts

robo = Robo(random.randint(0,10), random.randint(0,10))
#Ver onde o robo está naquele momento
str(robo)

# Loop for para que o jogador possa movimentar o robo por 10 vezes.
for i in range(10):
    movimento = input("Digite up, down, left ou right para se movimentar: ")
    if movimento == 'up':
        robo.mover_cima()
    
    elif movimento == 'down':
        robo.mover_baixo()
    
    elif movimento == 'left':
        robo.mover_esquerda()
    
    elif movimento == 'right':
        robo.mover_direita()
    
    else:
        print("\nVocê digitou um movimento que não existe! Tente novamente.")
        continue #para que o usario possa retornar para o inicio do loop for.
    
    print(robo)
    check_gift(robo, gifts)
