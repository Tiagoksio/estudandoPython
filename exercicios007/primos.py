# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo;
num = int(input('Informe um número: '))
multiplos = 0
for contador in range (2, num):
    if num % contador == 0: 
        multiplos += 1
if multiplos == 0:
    print('O número {} é primo'.format(num))
else:
    print('O número {} não é primo'.format(num))