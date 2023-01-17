'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''
print('    \33[1;35mGERADOR DE PA\33[m')
print('='*20)
pa = int(input('Digite o Termo: '))
r = int(input('Digite a Razão: '))
t = pa
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(t, end=' -> ')
        t += r
        cont += 1
    print('Pausa')
    mais = int(input('Quer mostrar mais algum termo: '))
print(f'FIM, total de {total} termos')



