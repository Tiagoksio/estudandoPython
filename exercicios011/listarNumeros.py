# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#   1. Quantos números foram digitados;
#   2. A lista de valores, ordenada de forma decrescente;
#   3. Se o valor 5 foi digitado e está ou não na lista.
lista = list()
while True:
    lista.append(int(input('Informe um número inteiro: ')))
    continuar = input('Deseja continuar?[S/N] ').strip().upper()
    if continuar == 'N':
        break
lista.sort(reverse = True)
print(f'Foram informados {len(lista)} números\nOs números em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O número 5 foi cadastrado nas posições: ', end='')
    for c in range(0, lista.count(5)):
        print(f'{lista.index(5) + c}', end=', ')
    print('\n')
else:
    print('O número 5 não foi inserido na lista.')