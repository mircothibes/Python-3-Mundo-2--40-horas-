'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''
from time import sleep
print('='*32)
print('PROGRAMA PARA CALCULAR FATORIAL')
print('='*32)
sleep(1)
numero = int(input('Digite um numero a ser calculadao: '))
print('CALCULANDO.....')
sleep(2)
c = numero
f = 1
while c > 0:
    print(f'{c}', end="")
    print(' x ' if c > 1 else ' = ', end=" ")
    f *= c
    c -= 1
print(f'{f}')
print('\33[1;36m''O FATORIAL do numero {} é {}'.format(numero, f))




