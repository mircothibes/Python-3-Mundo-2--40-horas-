'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
v = 0
while True:
    vc = int(input('Escolha um numero: '))
    pc = randint(0, 10)
    total = vc + pc
    t = ' '
    while t not in 'PI':
       t = str(input('Par/Impar: ')).strip().upper()[0]
    print(f'Vc jogou {vc} e o computador jogou {pc}. E o total foi de {total}')
    print('Deu Par' if total % 2 == 0 else 'Deu Impar')
    if t == 'P':
        if total % 2 == 0:
            print('Você venceu!!!')
            v += 1
        else:
            print('Voce Perdeu!!!')
            break
    elif t =='I':
        if total % 2 == 1:
            print('Você venceu!!!')
            v += 1
        else:
            print('Voce Perdeu!!!')
            break
    print('Vamos jogar novamente?')
print(f'Voce venceu {v} vezes!')
