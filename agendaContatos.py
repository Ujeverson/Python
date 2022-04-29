import csv

#Função que cria contatos
def criarContato():
    print("\nDigite as informações do contato")
    pessoa = input("Nome: ")
    mail = input("e-mail: ")
    tel = input("telefone: ")
    return pessoa, mail, tel

#função que cria e salva os dados como arquivo .csv
def salvarContato(pessoa, mail, tel):
    arquivo = open('contatos.csv', 'a')   #'a' escreve os dados ao final da linha, o 'w' sobrescreve
    arquivo.write('{},{},{}\n' .format(pessoa, mail, tel)) #\n para pular uma linha 
    arquivo.flush()
    arquivo.close()
    
p, e, t = criarContato()

salvarContato(pessoa=p,mail=e,tel=t)



