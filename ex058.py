'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''

import random
pc = random.randint(1, 10)
acertou = False
palpite = 0
print('---'*10)
print('     JOGO DA ADVINHAÇÃO')
print('---'*10)
while not acertou:
    jogado = int(input('Escolha um numero de 1 a 10 : '))
    palpite += 1
    if pc == jogado:
        acertou = True
    else:
        if jogado < pc:
            print('mais')
        else:
            print('menos')
print(f'Voce acertou e teve {palpite} palpites')







