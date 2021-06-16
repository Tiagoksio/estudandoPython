# Crie um programa onde o usuário possa digitar vários valores numéricos e os cadastre em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente;
lista = list()
while True:
    while True:
        num = int(input('Informe o número: '))
        if not num in lista:
            lista.append(num)
            break
        else:
            print(f'O número {num} já foi cadastrado.', end='')
    continuar = input('Deseja continuar?[S/N] ').strip().upper()
    if continuar == 'N':
        break
lista.sort()
print(f'Os valores cadastrados foram: {lista}')