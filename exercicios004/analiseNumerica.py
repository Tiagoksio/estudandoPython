num = int(input('Informe um número entre 0 e 9999: '))
if num > 9999 or num < 0:
    print('Número inválido!')
else:
    print('{:=^50}'.format(' Análise Numerica '))
    print('{:<15}{:<10}{:>10}{:>15}'.format('Milhar', 'Centena', 'Dezena', 'Unidade'))
    print('{:>6}{:>16}{:>13}{:>15}'.format(num // 1000 % 10, num // 100 % 10, num // 10 % 10, num // 1 % 10))