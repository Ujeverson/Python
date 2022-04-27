'''Utilizando as funções list() e zip() e loop for para poder relacionar uma
temperatura Celsius e Fahrenheit, e vice-versa, de forma mais simples.
'''

'''Função 1 - Recebe uma temperatura como parâmetro e retorna a 
temperatura em Fahrenheit'''
def fahrenheit(T): #T: temperatura
    return round(((float(9)/5)*T + 32), 2)

'''Função 2 - Recebe uma temperatura como parâmetro e retorna 
a temperatura em Celsius'''
def celsius(T): #T: temperatura
    return round((float(5)/9)*(T-32), 2)

#lista de temperaturas. Na próxima "versão" vou usar entradas de usuário.
temperaturas = [-5, 0, 27.5, 35, 100]


convertF = list(map(fahrenheit, temperaturas))
#print(convertF)

converC = list(map(celsius,temperaturas))
#print(converC)

print("\nConvertendo as temperaturas Fahrenheit em Celsius, temos:")
for i, v in zip(temperaturas,converC):
    print("\n",i,"°F =",v,"°C")

print("\nConvertendo as temperaturas Celsius em Fahrenheit, temos:")
for i, v in zip(temperaturas,convertF):
    print("\n",i,"°C =",v,"°F")