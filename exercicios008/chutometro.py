# Usando o while, faça um programa onde o usuário possa chutar um número aleatório entre 0 e 10 que o computador gerou. No final, mostre quantos palpites foram necessários para acertar;
from random import randint
numGerado = randint(0, 10)
palpite = 99
numChutes = 0
while palpite != numGerado:
    numChutes += 1
    palpite = int(input('Tente acertar o número gerado, informe um número inteiro entre 0 e 10: '))
    if palpite != numGerado:
        print('Número incorreto. Tente novamente!')
print(f'Exatemente {palpite}, você acertou em {numChutes} tentativas!')