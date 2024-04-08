import random
from bubble_sort import bubble_sort


def test():
    any_numbers = random.sample(range(1,1000), 42)
    alredy_sorted = [1,2,3,4,5,6,7,8,9,20,22,25,28,33,45,47,80,81,200]
    inversed = [200,81,80,47,45,33,28,25,22,20,9,8,7,6,5,4,3,2,1]
    repeated = [7,7,7,7,7,1,1,9,9,0,4,4,4,5,4,5,7,1]

    print('\0 Números aleatórios: ', any_numbers)
    bubble_sort(any_numbers)
    print('\0 Números ordenados: ', any_numbers)


    print('\0 Números já ordenados: ', alredy_sorted)
    bubble_sort(alredy_sorted)
    print('\0 Números ordenados: ', alredy_sorted)


    print('\0 Números invertidos: ', inversed)
    bubble_sort(inversed)
    print('\0 Números ordenados: ', inversed)

    print('\0 Números repitidos: ', repeated)
    bubble_sort(repeated)
    print('\0 Números ordenados: ', repeated)

test()