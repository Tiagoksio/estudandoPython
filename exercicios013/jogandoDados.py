# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado;
from random import randint
from time import sleep

jogador = dict()
resultado = list()
for k in range(1, 5):
    jogador['nome'] = input(f'Informe o nome do {k}º jogador: ').strip()
    jogador['dado'] = randint(1, 6)
    print(f'O jogador {jogador["nome"]} tirou {jogador["dado"]}')
    resultado.append(jogador.copy())
for cont in range(0, len(resultado) - 1):
    for cont2 in range(cont, len(resultado)):
        if cont == cont2:
            continue
        elif resultado[cont]['dado'] < resultado[cont2]['dado']:
            temp = resultado[cont].copy()
            resultado[cont] = resultado[cont2].copy()
            resultado[cont2] = temp.copy()
print(f'Os resultados foram...')
sleep(0.7)
for indice in range(0, len(resultado)):
    print(f'{indice + 1}ª lugar ficou o jogador {resultado[indice]["nome"]} com {resultado[indice]["dado"]}')
'''
Poderia fazer também utilizar os métodos sorted() e itemgetter() from operator e utilizar o reverse=True para ordenar em ordem decrescente.
#itemgetter(0 = key, 1 = value)
EX: ranking = list()
ranking = sorterd(jogo.items(), key=itemgetter(1))# para ordenar por valor 
'''