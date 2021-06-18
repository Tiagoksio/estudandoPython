# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e impares em ordem crescente.
lista = list()
for num in range(0, 7):
    lista.append(int(input(f'Informe o {num + 1}º número: ')))
lista.sort()
print('Os valores pares foram: ', end='')
for num in lista:
    if num % 2 == 0:
        print(f'{num}... ', end='')
print('\nOs valores impares foram: ', end='')
for num in lista:
    if num % 2 != 0:
        print(f'{num}... ', end='')
print('\n')
'''
Gabarito
num = [[], []]
valor = 0
for c in range(1, 8)
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')
'''