# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número entre 0 e 20 e mostrá-lo por extenso;
numExtenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
while True:
    num = int(input('Informe um número entre 0 e 20: '))
    if num < len(numExtenso) and num >= 0:
        break
    print('Valor inválido. ', end='')
print(f'Você digitou o número "{numExtenso[num].capitalize()}"')