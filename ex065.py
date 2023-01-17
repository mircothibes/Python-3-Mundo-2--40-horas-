'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
'''
v = cont = soma = 0
v = int(input('Digite um valor: '))
while v != 0:
    soma += v
    cont += 1
    v = int(input('Digite um valor: '))
print('FIM')
print(f'A soma dos valores digitados da \33[1:33m{soma}\33[m, e foram digitadas \33[1:33m{cont}\33[m vezes')
'''

r = 'S'
soma = quantidade = media = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Você que continuar? [S/N] ')).strip().upper()[0]
media = soma / n
print('FIM')
print(f'Foi digitado {quantidade} numeros e média dos valores é de {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')




