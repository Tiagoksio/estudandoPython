# SELECTION SORT - Algoritmo de seleção -> Ultilizado para ordenar uma lista
import random

def selection_sort(list):
    for j in range (len(list)-1):
        min_index = j
        for i in range(j, len(list)):
            if list[i] < list[min_index]:
                min_index = i
        if list[j] > list[min_index]:
            aux = list [j]
            list[j] = list [min_index]
            list[min_index] = aux
    
def test():
    any_numbers = random.sample(range(1,1000), 42)
    alredy_sorted = [1,2,3,4,5,6,7,8,9,20,22,25,28,33,45,47,80,81,200]
    inversed = [200,81,80,47,45,33,28,25,22,20,9,8,7,6,5,4,3,2,1]
    repeated = [7,7,7,7,7,1,1,9,9,0,4,4,4,5,4,5,7,1]

    print('Números aleatórios: ', any_numbers)
    selection_sort(any_numbers)
    print('Números ordenados: ', any_numbers)


    print('Números já ordenados: ', alredy_sorted)
    selection_sort(alredy_sorted)
    print('Números ordenados: ', alredy_sorted)


    print('Números invertidos: ', inversed)
    selection_sort(inversed)
    print('Números ordenados: ', inversed)

    print('Números repitidos: ', repeated)
    selection_sort(repeated)
    print('Números ordenados: ', repeated)

test()
    