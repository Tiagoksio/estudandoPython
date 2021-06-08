# Crie um programa que leia o ano de nascimento de sete pessoas, no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores;
from datetime import date
pessoas = []
maiores = 0
menores = 0
for cadPessoa in range (0, 7):
    pessoas.append(date.today().year - int(input('Informe o ano de nascimento da {}º pessoa: '.format(cadPessoa + 1))))
    if pessoas[cadPessoa] >= 18:
        maiores += 1
    else:
        menores += 1 

print('Foram observados {} maiores de idade e {} menores.'.format(maiores, menores))
