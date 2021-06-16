# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições;
lista = list()
for count in range(1, 6):
    lista.append(int(input(f'Informe o {count}º valor: ').strip()))
print(f'O maior valor informado foi o "{max(lista)}", que se encontra da posição "{lista.index(max(lista))}"')
print(f'O menor valor informado foi o "{min(lista)}", que se encontra da posição "{lista.index(min(lista))}"')