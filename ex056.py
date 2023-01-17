'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
a média de idade do grupo,
qual é o nome do homem mais velho
e quantas mulheres têm menos de 20 anos.'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulheres20 = 0
for c in range(1, 5):
    print(f'A {c}ª pessoa:')
    nome = str(input('Qual o seu nome: ')).strip()
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual o seu sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulheres20 += 1
mediaidade = somaidade / 4
print(f'A media de idade do grupo é de {mediaidade} anos!!!')
print(f'A idade do homem mais velho é {maioridadehomem} anos, e o seu nome é {nomevelho}!!!')
print(f'Ao todo são {totalmulheres20} mulheres menores que 20 anos!!!')





