# - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu **preço normal** e **condição de pagamento**:
#     - À vista dinheiro/cheque: 10% de desconto;
#     - À vista cartão: 5% de desconto;
#     - Em até 2x no cartão: preço normal;
#     - 3x ou mais no cartão: 20% de juros;
preco = float(input('Informe o preço do produto: '))
formadePag = int(input('Informe o meio de pagamento:\n1 - À vista dinheiro/cheque: 10% de desconto;\n2 - À vista cartão: 5% de desconto;\n3 - Em até 2x no cartão: preço normal;\n4 - 3x ou mais no cartão: 20% de juros;\nSelecione a opção: '))
if formadePag == 1:
    print('O produto sairá por R${}.'.format(preco - preco * 0.1))
elif formadePag == 2:
    print('O produto sairá por R${}.'.format(preco - preco * 0.05))
elif formadePag == 3:
    print('O produto sairá por R${}.'.format(preco))
else:
    print('O produto sairá por R${}.'.format(preco + preco * 0.2))