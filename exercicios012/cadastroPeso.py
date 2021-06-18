# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#   1. Quantas pessoas foram cadastradas;
#   2. Uma listagem com as pessoas mais pesadas;
#   3. Uma listagem com as pessoas mais leves.
def ordenar(index, num, lista):
    if index == len(lista) or lista[index] > num:
        return index
    else:
        return ordenar(index + 1, num , lista)

pessoas = list()
pes = ['nome', 00.0]
pessoas_peso = list()

while True:
    pes[0] = input('Informe o nome: ').strip()
    pes[1] = float(input('Informe o peso: '))
    pessoas.append(pes[:])
    continuar = input('Deseja continuar?[S/N] ').strip().upper()
    if continuar == 'N':
        break
for individuo in pessoas:
    pessoas_peso.insert(ordenar(0, individuo[1], pessoas_peso), individuo[1])


print(f'\nForam cadastradas {len(pessoas)} pessoas\nAs mais leves para as mais pesadas são: ')
for peso in pessoas_peso:
    for pessoa in pessoas:
        if peso == pessoa[1]:
            print(f'{pessoa[0]} com KG {peso}')