dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos KMs foram percorridos com o carro? '))
print('O total a ser pago é R${:.2f}'.format(dias * 60 + km * 0.15))