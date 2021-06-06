# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sia idade:
#   Se ele ainda vai se alistar ao serviço militar;
#   Se é a hora de se alistar;
#   Se já passou do tempo do alistamento;
#   O tempo que falta ou prazo que passou do prazo.
from datetime import date
nasc = int(input('Informe em que ano você nasceu: '))
idade = date.today().year - nasc
if idade < 18:
    print('Ainda faltam {} ano[s] para você se alistar.'.format(18 - idade))
elif idade == 18:
    print('Você está no periodo de alistamento')
else:
    print('Já passaram {} ano[s] do seu alistamento.'.format(idade - 18))