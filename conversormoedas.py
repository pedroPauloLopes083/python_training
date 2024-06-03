taxa_cambio = 5.00

valor_real = float(input("""
                         Insira o valor em Reais a ser convertido para Dólares 
                         (Utilize '.' para separar as casas decimais): 
                         """
                         ))

valor_convertido = valor_real * taxa_cambio

print(f"O valor inserido em Reais equivale a {valor_convertido:.2f} Dólares, considerando a taxa de câmbio de {taxa_cambio:.2f}")