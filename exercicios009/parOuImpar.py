# Faça um programa que jogue par ou impar com o usuário e só pare quando o mesmo perder. No final, mostre quantas vitórias consecutivas ele consquistou;
from random import randint
vitorias = 0
while True:
    computador = randint(1, 20)
    while True:
       pOuiJogador = input('Deseja "PAR" ou "IMPAR"[P/I]: ').strip().upper()
       numJogador = int(input('Informe o número: '))
       if (pOuiJogador == 'P' or pOuiJogador == 'I') and numJogador >= 0:
           break
    if (numJogador + computador) % 2 == 0 and pOuiJogador == 'P':
        print(f"Computador {computador} x {numJogador}\nA soma é {computador + numJogador}\nPAR, você venceu!")
        vitorias += 1
    elif (numJogador + computador) % 2 != 0 and pOuiJogador == 'I':
        print(f"Computador {computador} x {numJogador}\nA soma é {computador + numJogador}\nIMPAR, você venceu!")
        vitorias += 1
    elif (numJogador + computador) % 2 != 0:
        print(f"Computador {computador} x {numJogador}\nA soma é {computador + numJogador}\nIMPAR, você perdeu\nTotal de vitórias: {vitorias}")
        break
    else:
        print(f"Computador {computador} x {numJogador}\nA soma é {computador + numJogador}\nPAR, você perdeu\nTotal de vitórias: {vitorias}")
        break