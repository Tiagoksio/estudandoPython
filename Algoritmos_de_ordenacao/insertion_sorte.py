# Insertion sorte -> Odenação por inserção; Segue a lógica de ordenar cartas de um baralho na mão, onde você sempre insere os valores já de forma ordenada.
def insertion_sort(list):
    n = len(list)
    for i in range(1, n):
        chave = list[i]
        j = i - 1 # Lista já ordenada
        while j >= 0 and list[j] > chave:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = chave