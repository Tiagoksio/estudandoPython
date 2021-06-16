# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort());
def ordenar(index, num, array):
    if index == len(array) or array[index] > num:
        return index
    else:
        return ordenar(index + 1, num , array)
lista = list()           
for count in range(0,5):
    num = int(input(f'Informe o {count + 1}º número: '))
    lista.insert(ordenar(0, num, lista), num)
print(f'Os números informados em ordem são: {lista}')