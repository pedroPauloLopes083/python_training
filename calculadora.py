def calculadora():
    operacao = int(input("""Escolha a operação que deseja fazer: . 
                        Use 1 para Adição
                        Use 2 para Subtração
                        Use 3 para Divisão
                        Use 4 para Multiplicação : """))
    
    num1 = float(input("Insira o primeiro número para realizar a operação: "))
    num2 = float(input("Insira o segundo  número para realizar a operação: "))
    
    if operacao == 1:
        resultado = num1 + num2
        operacao = "adição"
    elif operacao == 2:
        resultado = num1 - num2
        operacao = "subtração"
    elif operacao == 3:
        resultado = num1 / num2
        operacao = "divisão"
    elif operacao == 4:
        resultado = num1 * num2
        operacao = "multiplicação"
        
    print(f"O resultado da operação de {operacao} é {resultado:.2f}.")
        
calculadora()