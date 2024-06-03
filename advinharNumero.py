import random

numero_random = random.randint(1,100)
Tentativas = 0
Tentativas_restantes = 10

while True:
    
    palpite = int(input(f"""
                        Advinhe um número aleatório de 1 a 100.
                        Você tem {Tentativas_restantes} tentativas restantes.
                        Insira o seu palpite:  
                        """))
    Tentativas += 1
    Tentativas_restantes -= 1
    
    if Tentativas_restantes == 0:
        print("Você excedeu as 10 tentativas possíves. Fim do jogo.")
        break
    
    if palpite < numero_random:
        print(f"Seu palpite: {palpite}. Tente um número maior")
    
    elif palpite > numero_random:
        print(f"Seu palpite: {palpite}. Tente um número menor")
    
    else:
        print(f"Parabéns! Você acertou! O número correto é {numero_random}")
        print(f"Foram necessárias {Tentativas} tentativas para acertar")
        break
    
