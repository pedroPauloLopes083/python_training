def contarVogais(str):
    while True:
        palavra = input("Insira a sua palavra aqui: ")
        if palavra.isalpha(): 
            break
        else:
            print("Por favor, insira uma palavra válida.")
    
    vogais = "aeiouAEIOUáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãõÃÕàèìòùÀÈÌÒÙ"
    contar_v = 0
    contar_c = 0

    for letra in palavra:
        if letra in vogais:  
            contar_v += 1
        else:
            contar_c += 1
            
    if contar_v == 0:
        print(f"A palavra {palavra} não possui nenhuma vogal")
        print(f"A palavra {palavra} possui {contar_c} consoantes")
    elif contar_c == 0:
        print(f"A palavra {palavra} não possui nenhuma consoante")
        print(f"A palavra {palavra} possui {contar_v} vogais")
    else:    
        print(f"A palavra {palavra} possui {contar_v} vogais")
        print(f"A palavra {palavra} possui {contar_c} consoantes")



contarVogais(str)
