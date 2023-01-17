''' Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais'''

n1 = int(input('\33[1;33mprimeiro numero:\33[m '))
n2 = int(input('\33[1;33msegundo numero:\33[m '))
if n1 > n2:
    print('\33[1;32mO valor {:.0f}, que é o primeiro valor, é maior que o valor {:.0f}!\33[m'.format(n1, n2))
elif n2 > n1:
    print('\33[1;31mO valor {:.0f}, que é o segundo valor,   é maior que o valor {:.0f}!\33[m'.format(n2, n1))
else:
    print('\33[1;30mNão existe valor maior, os dois são iguais!!!!\33[m')


