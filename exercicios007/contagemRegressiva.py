# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles;
from time import sleep
from pygame import mixer

iniciar = input('Deseja iniciar? [s/n]').lower()
if iniciar == 's':
    for contando in range (10, -1, -1):
        print('{}...'.format(contando))
        sleep(0.5)
    print('FELIZ ANO NOVO!!!')
    mixer.init()
    musica = mixer.Sound('caminho-do-arquivo/fireworks.ogg')
    musica.play(-1)
    parar = input('APERTE QUALQUER TECLA PARA SAIR...')
