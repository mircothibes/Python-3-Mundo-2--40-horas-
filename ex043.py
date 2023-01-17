'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''
print('\33[1;44m=+=\33[m'*40)
print('                                        \33[1;33;34mCALCULADORA DE IMC\33[m')
print('\33[1:44m=+=\33[m'*40)

peso = float(input('Qual é o seu peso (KG): '))
altura = float(input('Qual é a sua altura (m): '))
imc = peso / (altura ** 2)
print('O seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo')
elif 18.5 <= imc < 25:
    print('Ideal')
elif imc <= 25 < 30:
    print('Sobrepeso')
elif imc <= 30 < 40:
    print('Obesidade')
else:
    print('Você está morrendo, desgraça!!!!')


