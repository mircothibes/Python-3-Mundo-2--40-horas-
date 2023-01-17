'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

op = 0
valoru = int(input('Digite o primeiro valor: '))
valord = int(input('Digite o segundo valor: '))
print('='*10)
while op != 5:
    print(''' [1] somar
 [2] multiplicar
 [3] maior
 [4] novos numeros
 [5] sair''')
    print('=' * 10)
    op = int(input('Qual sua opção? '))
    if op == 1:
        soma = valoru + valord
        print(f'A soma entre {valoru} e {valord} é igual a {soma}')
    elif op == 2:
        multi = valoru * valord
        print(f'O valor {valord} x {valoru} é igual {multi}')
    elif op == 3:
        if valoru > valord:
            print(f'O valor {valoru} é maior que {valord}')
        elif valoru == valord or valord == valoru:
            print('Os valores sao iguais!')
        else:
            print(f'O valor {valord} é maior que o valor {valoru}')
    elif op == 4:
        valoru = int(input('Digite o primeiro valor: '))
        valord = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('=' * 10)
    else:
        print('Opção invalida, tente novamente!')
print('Saindo....')









