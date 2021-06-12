# Escreva um programa que leia um número inteiro e mostre na tela os n primeiros elementos de uma sequência fibonacci;
num = int(input('Informe quantos números da sequência fibonacci deseja consultar: '))

num1 = num2 = contador = 1

while contador <= num:
    if contador == 1 or contador == 2:
        print(f'{contador}º termo: {1}')
        contador += 1
    else:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        print(f'{contador}º termo: {num3}')
        contador += 1