# Desenvolva um programa que leia 4 valores e guarde-os em uma tupla. No final, mostre:
#    1. Quantas vezes apareceu o valor 9;
#    2. Em que posição foi digitado o primeiro valor 3;
#    3. Quais foram os números pares.
num = (int(input('Informe o primeiro número: ')), int(input('Informe o segundo número: ')), int(input('Informe o terceiro número: ')), int(input('Informe o quarto número: ')))

if 3 in num:
    print(f'O número 3 se encontra na posição {num.index(3)}')
else:
    print(f'Não foi inserido o número 3')
print(f'O numero 9 aparece {num.count(9)} vez(es)')
print('Os números pares são: ', end='')
for par in num:
    if par % 2 == 0:
        print(f'{par} ', end='')