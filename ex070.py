''' Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

totgasto = tot1000 = menor = cont = 0
barato = ' '
while True:
    print('=' * 40)
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preço = float(input('Digite o preço do produto em Reais(R$): '))
    cont += 1
    totgasto += preço
    if preço > 1000:
        tot1000 += 1
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    print('=' * 40)
    decisao = ' '
    while decisao not in 'SN':
        decisao = str(input('Voce gostaria de conitnuar? [S/N]')).strip().upper()
    if decisao == 'N':
        print('=' * 40)
        print('Programa Terminado!!!')
        print('=' * 40)
        break
print(f'O total gasto nas compras é de {totgasto:.2f}')
print(f'Tem {tot1000} produtos custando mais que R$ 1.000,00')
print(f'O produto mais barato é {barato} que custa R${menor:.2f}')
