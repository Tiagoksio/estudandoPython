# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
notas50 = notas20 = notas10 = notas1 = 0
acumulador = 0

print(f'{" CAIXA ELETRÔNICO ":-^40}')
saque = int(input('Quanto deseja sacar: '))
notas50 = saque // 50
acumulador = saque % 50
notas20 = acumulador // 20
acumulador %= 20
notas10 = acumulador // 10
acumulador %= 10
notas1 = acumulador // 1
print(f'Saque no valor de R${saque} realizado\nNOTAS:\nR$50,00: {notas50}\nR$20,00: {notas20}\nR$10,00: {notas10}\nR$1,00: {notas1}')