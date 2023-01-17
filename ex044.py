'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format('LOJAS LOJAS'))

produto = float(input('Digite o valor do produto: R$'))
print('''Formar de Pagamento
[1] à vista
[2] à vista parcelado
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção: '))

if opção == 1:
    a_vista = produto - (produto * 10 / 100)
    print('O valor do produto é de \33[1;36mR${:.2f}\33[m, '
      'e a vista ou no cheuque com 10% de desconto o valor fica \33[1;36mR${:.2f}\33[m'.format(produto, a_vista))
elif opção == 2:
    no_cartao = produto - (produto * 5 / 100)
    print('O valor do produto é de \33[1;36mR${:.2f}\33[m, '
      'e a vista ou no cartão com 5% de desconto o valor fica \33[1;36mR${:.2f}\33[m'.format(produto, no_cartao))
elif opção == 3:
    duas_cartao = produto
    print('O valor do produto é de \33[1;36mR${:.2f}\33[m, '
      'e em ate 2x no cartão o valor fica \33[1;36mR${:.2f}\33[m'.format(produto, duas_cartao))
elif opção == 4:
    tres_cartao = produto + (produto * 20 / 100)
    print('O valor do produto é de \33[1;36mR${:.2f}\33[m, '
      'e em 3x no cartão o valor fica \33[1;36mR${:.2f}\33[m'.format(produto, tres_cartao))
else:
    opção = 0
    print('Opção invalida')





