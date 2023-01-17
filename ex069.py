'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

tot18 = 0
toth = 0
totm = 0
while True:
    print('=' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Voce deseja continuar? [Sim/Não] ')).strip().upper()[0]
    print('=' * 30)

    if resp == 'N':
        print('Tchau')
        break
print(f'O numero de pessoas maior que 18 anos é de {tot18}')
print(f'O numero total de homens é {toth}')
print(f'O numero total de mulheres menores de 20 ano é de {totm}')


