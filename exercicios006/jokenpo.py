# Crie um programa que faça o computador jogar jokenpô com você.
from random import randint
from time import sleep
mao = ['Pedra', 'Papel', 'Tesoura']
pc = randint(0,2)
jogador = int(input('Jogadas:\n0 - Pedra\n1 - Papel\n2 - Tesoura\nSelecione a sua jogada: '))
if jogador < 0 or jogador > 2:
    print('Opção inválida')
else:
    print("\nJO...")
    sleep(0.8)
    print("KEN...")
    sleep(0.8)
    print("PÔ!!!!\n")
    print("=" * 35)

    print('\033[1;36mJogador\033[m {} x {} \033[1;31mComputador\033[m'.format(mao[jogador], mao[pc]))
    print("=" * 35)

    if pc == jogador:
        print('\033[0;33mEmpate\033[m')
    elif pc == 0 and jogador == 2 or pc == 1 and jogador == 0 or pc == 2 and jogador == 1:
        print('\033[0;31mO computador Venceu!\033[m')
    else:
        print('\033[0;32mVocê venceu!\033[m')