''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

total = 0
numero = int(input('Digite um numero inteiro: '))
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\33[34m', end='')
        total += 1
    else:
        print('\33[31m', end='')
    print(f'{c}', end=' - ''\33[m')
print(f'Acabou!!!'
      f'O numero {numero} foi divisível {total} vezes')
if total == 2:
    print(f'O numero {numero} é PRIMO!!!!!!')
else:
    print(f'E por isso que o numero {numero} não é PRIMO')

