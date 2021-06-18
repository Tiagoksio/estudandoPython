# Faça um programa que ajude um jogador MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta;
from random import randint
from time import sleep
jogos = list()
jogo = list()
totJogos = int(input('Quantos jogos deseja? '))
for n in range(0, totJogos):
    for n in range(1, 7):
        jogo.append(randint(1,60))
    jogos.append(jogo[:])
    jogo.clear()
print(f'Seus jogos são: ')
for num, j in enumerate(jogos):
    sleep(0.7)
    print(f'Jogo {num + 1}: {j}')
    