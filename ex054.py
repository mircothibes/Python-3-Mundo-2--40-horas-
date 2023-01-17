'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''

from datetime import date
tempo = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8,):
    anos = int(input('Digite o ano: '))
    print(f'A {c}ª pessoa nasceu no ano de {anos}')
    maioridade = tempo - anos
    print(f'E esta pessoa tem {maioridade} anos')
    if maioridade >= 18:
        totalmaior += 1
        print('E ela é Maior de idade!')
    else:
        totalmenor += 1
        print('E ela é Menor de idade!')
print(f'\33[1:34mNo total tivemos {totalmaior} pessoas MAIORES e {totalmenor} pessoas MENORES!!\33[m')















