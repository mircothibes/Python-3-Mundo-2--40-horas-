'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
atual = date.today().year
nasc = int(input('Qual é o ano de nascimento: '))
idade = atual - nasc
if idade == 18:
    print('Você já se alistou recruta? estamos precisando de você, chegou a sua hora!!!')
elif idade < 18:
    print('Já já chegará sua hora pequeno soldado!!!E falta apenas {} anos para você se juntar a gente!!!'.format(18 - idade))
else:
    print('Voce tera que comparecer ao quartel soldado!!! e já passou {} anos do seu alistamento'. format(idade - 18))
