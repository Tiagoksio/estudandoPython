# SELECTION SORT - Algoritmo de seleção -> Ultilizado para ordenar uma lista levando o menor valor para o inicio da lista
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