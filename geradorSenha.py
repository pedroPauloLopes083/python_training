import random
import string

def gerador_de_senhas(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
nova_senha = gerador_de_senhas(tamanho_senha)

print(f"Sua senha segura: {nova_senha}")