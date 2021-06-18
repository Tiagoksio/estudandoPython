# - Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta. Mostre também:
#     1. A soma de todos os valores pares;
#     2. A soma dos valores da terceira coluna;
#     3. O maior valor da segunda linha.
matriz = [[[],[],[]],[[],[],[]],[[],[],[]]]
somaPar = 0
somaTerCol = 0
maiorSegLin = 0
for h in range(0,3):
    for v in range(0,3):
        num = int(input(f'Informe o número para a cordenada "{h}{v}": '))
        if num % 2 == 0:
            somaPar += num
        if v == 2:
            somaTerCol += num
        if h == 1 and num > maiorSegLin:
            maiorSegLin = num
        matriz[h][v].append(num)
for h in range(0,3):
    for v in range(0,3):
        print(f'{matriz[h][v]} ', end='')
    print('\n')
print(f'A soma dos valores pares é: {somaPar}')
print(f'A soma dos valores da terceira coluna são: {somaTerCol}')
print(f'O maior valor da segunda linha é: {maiorSegLin}')