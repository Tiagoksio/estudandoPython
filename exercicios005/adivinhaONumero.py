#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e pela para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa devera escrever na tela se o usuário venceu ou perdeu;
from random import randrange
def check(numero, palpite):
    if numero == palpite:
        print('Parabéns, você acertou!')
    else:
        palpite = int(input('Tente novamente: '))
        check(numero, palpite)
num = randrange(0, 6)
chute = int(input('Adivinha o número entre 0 e 5 que eu estou pensando: '))
check(num, chute)