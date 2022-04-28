#Função que cria contatos
import email


def criacontato():
    print("Digite as informações do contato")
    nome = input("Nome: ")
    email = input("e-mail: ")
    telefone = input("telefone: ")
    
    return nome, email, telefone

nome, email, telefone = acriacontato()

#criar e salva os dados como arquivo .csv
contatos = open('contatos.csv','w')
contatos.write('%s,%s,%s' % (nome, email, telefone))
contatos.flush()
contatos.close()



