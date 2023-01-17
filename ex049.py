'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''

num = int(input('Digite seu numero para a taboada: '))
for t in range(1, 11):
    print(f'{num} x {t} = {num*t}')


