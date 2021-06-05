# Faça um programa que leia um ano qualquer e mostre se ele é **Bissexto**;
from datetime import date
ano = int(input('Informe o número do ano ou "0" para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
print("O ano {} é BISSEXTO".format(ano) if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else "O ano {} não é BISSEXTO".format(ano))