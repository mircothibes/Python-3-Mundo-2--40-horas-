'''Crie um programa que faça o computador jogar Jokenpô com você.'''


from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('QUal é sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('O computador escolheu {}'.format(itens[computador]))
print('Jogador jogou a opção {}'.format(itens[jogador]))
if computador == 0: # Computador Jogou Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador Vence')
    else:
        print('Jogada Invalida!!!')

elif computador == 1: # Computador Jogou Papel
    if jogador == 0:
        print('Computador Vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('Jogada Invalida!!!')

elif computador == 2: # Computador Jogou Tesoura
    if jogador == 0:
        print('O Jogador Vence')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Invalida!!!')