# Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final, mostre os 10 primeiros termos dessa progressão;
progressao = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão da progressão aritmética: '))
for num in range(0, 10):
    print('{}'.format(progressao))
    progressao += razao