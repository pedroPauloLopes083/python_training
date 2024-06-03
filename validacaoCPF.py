def validacaoCPF():
    
    while True:
        CPF = input("Insira o seu CPF. Utilize apenas números: ")
        if len(CPF) == 11 and CPF.isdigit():
            CPF_formatado = f"{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}"
            print(f"{CPF_formatado} é um CPF válido.")
            break
        else:
            print(f"Erro. {CPF} é um CPF inválido.") 
            print("Por favor, tente mais uma vez. Utilize apenas números.")
            
validacaoCPF()
