'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Digite o sexo [Masculino/Feminino]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados incorretos, favor digitar denovo: ')).strip().upper()[0]
else:
    print(f'sexo digitado é o de {sexo}!!!')
