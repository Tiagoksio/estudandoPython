# Faça um programa que leia 3 números e escreva qual é o **maior** e  qual é o **menor**;
contador = 0
num = []
while contador < 3:
    num.append(int(input('Informe o {}º número: '.format(contador + 1))))
    contador += 1
num = sorted(num)
print('O maior número é: {}\nO menor é: {}'.format(num[2], num[0]))    