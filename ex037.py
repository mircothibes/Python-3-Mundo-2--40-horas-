'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input('Digite um numero: '))
print('''Escolha uma das bases para a conversão:
\33[1;31m[ 1 ] converter para BINARIO
\33[1;31m[ 2 ] converter para OCTAL
\33[1;31m[ 3 ] converter para HEXADECIMAL\33[m''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINARIO é igual a {}'. format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido pra OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida')


