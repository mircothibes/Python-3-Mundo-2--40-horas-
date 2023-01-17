''' Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

pa = int(input('Primeiro termo: '))
r = int(input('Qual é a razão: '))
decimo = pa + (10 - 1) * r
for c in range(pa, decimo + r, r):
    print(f'{c}', end=' = ')
print('ACABOU!!!')

