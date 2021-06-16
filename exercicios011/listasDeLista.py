# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas;
lista = list()
listaPar = list()
listaImpar = list()
while True:
    lista.append(int(input('Informe um número inteiro: ')))
    continuar = input('Deseja continuar?[S/N] ').strip().upper()
    if continuar == 'N':
        break
for num in lista:
    if num % 2 == 0:  
        listaPar.append(num)
    else:
        listaImpar.append(num)

print(f'Os números cadastrados são: {lista}\nOs números pares são: {listaPar}\nOs números impares são: {listaImpar}')

