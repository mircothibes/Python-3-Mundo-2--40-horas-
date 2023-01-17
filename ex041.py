'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import date
data = date.today().year
nascimento = int(input('Digite o ano em que nasceu: '))
anos = data - nascimento
if anos <= 9:
    print('Você tem {} anos e sua categoria é MIRIM'.format(anos))
elif anos <= 14:
    print('Você tem {} anos e sua categoria é INFANTIL'.format(anos))
elif anos <= 19:
    print('Você tem {} anos e sua categoria é JUNIOR'.format(anos))
elif anos <= 25:
    print('Você tem {} anos e sua categoria é SENIOR'.format(anos))
else:
    print('Você tem {} anos e sua categoria é MASTER'.format(anos))




