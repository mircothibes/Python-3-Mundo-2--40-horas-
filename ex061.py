'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
 mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

pa = int(input('Digite o termo: '))
r = int(input('Digite e razão: '))
t = pa
cont = 1
while cont <= 10:
    print(t, end=' -> ')
    t += r
    cont += 1
print('Acabou!!!')
