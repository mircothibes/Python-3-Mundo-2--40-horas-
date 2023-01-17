''' Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.'''

pesomaior = 0
pesomenor = 0
for p in range(1, 6):
    peso = float(input(f'Qual é o seu peso da {p}ª pessoa: (KG)'))
    if p == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print(f'Peso maior é de {pesomaior}(KG)\n'
      f'Peso menor é {pesomenor}(KG)')



