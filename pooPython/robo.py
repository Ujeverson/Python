#Criar um robo que se movimenta em uma matriz 10 x 10
class Localizacao(object):
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

class Gift(Localizacao):
    def __init__(self, x, y, name): 
        super(Gift, self).__init__(x,y)
        self.name = name

class Robo(Localizacao):
        
    def mover_frente(self): #ou mover p cima
        
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



gift = Gift(2 , 2, 'moeda de prata')

robo1 = Robo(6, 6)


print("\n",robo1.y)