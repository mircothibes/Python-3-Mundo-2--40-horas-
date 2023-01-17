'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
print('-=-'*20)
print('\33[1;31m                EMPRESTIMO BANCÁRIO\33[m')
print('-=-'*20)

valor_casa = float(input('Qual é o valor da casa: '))
salario = float(input('Qual é o salario: '))
anos = int(input('Quantos anos para o pagamento: '))
prestação = valor_casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar um casa de R${:.2f} em {} anos'.format(valor_casa, anos), end='')
print(' a prestação sera de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('O emprestimo pode ser CONCEDIDO!!!')
else:
    print('O emprestimo foi NEGADO!!!')

