# Calculadora em Python


print("\n******************* Calculadora em Python  *******************")

#painel de escolha das operações
x = [1, 2, 3, 4]

while True:
    print("\n1 - Adição")
    print("\n2 - Subtração")
    print("\n3 - Multiplicação")
    print("\n4 - Divisão")
    
    #aqui o usuário escolhe umas das opções impressa acima
    opcao = int(input("\nEscolha a opção desejada ou 0, zero, para sair!\nObs: Digite apenas o número da opção."))
    
    #se o usuário escolher 0(zero) a calculadora fecha.
    if opcao == 0:
        break

    elif opcao in x:
        num1 = float(input("\nDigite o primeiro número:"))
        num2 = float(input("\nDigite o segundo número:"))
        if opcao == 1:
            print("\n###### A soma entre %.1f e %.1f é %.1f! ###### " %(num1, num2,num1 + num2))
            continue
        elif opcao == 2:
            print("\n###### A diferença entre %.1f e %.1f é %.1f! ###### " %(num1, num2,num1 - num2))
            continue
        elif opcao == 3:
            print("\n###### O produto entre %.1f e %.1f é %.1f! ###### " %(num1, num2,num1*num2))
            continue
        elif opcao == 4:
            print("\n###### O quociente entre %.1f e %.1f é %.1f! ###### " %(num1, num2,num1/num2))
            continue
        
    else:
        print("\nDIGITE UMA OPÇÃO VÁLIDA!")
        continue


    
    






