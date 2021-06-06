# Crie um programa que leia o ano de nacimento e classifique os atletas de acordo com a idade:
#   Até 9 anos: **"Mirim"**;
#   Até 14 anos: **"Infantil"**;
#   Até 19 anos: **"Junior"**;
#   Até 25 anos: **"Sênior"**;
#   Acima: **"Master"**.
from datetime import date
nasc = int(input('Informe em que ano você nasceu: '))
idade = date.today().year - nasc
if idade <= 9 :
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Junior')
elif idade <= 25:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')