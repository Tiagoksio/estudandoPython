# Bubble Sort - Algoritmo de bolha -> Ultilizado para ordenar uma lista flutuando os valores

def bubble_sort(list):
    for j in range(len(list)-1):
        for i in range(len(list)-1):
            if list[i] > list [i+1]:
                #Instrução em python que faz a troca dos números no arrey sem a necessidade da variável auxiliar // posições I e I+1
                list[i], list[i+1] = list[i+1],list[i] 