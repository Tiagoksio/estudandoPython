# Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar '999'. No final, mostre quantos números forma digitados e qual foi a soma entre eles, desconsiderando o flag (999);
contador = 0
acumulador = 0
num = 0
while True:
    contador += 1
    num = int(input(f'Informe o {contador}º número: '))
    if num == 999:
        break
    else:
        acumulador += num
print(f'Foram informados {contador - 1} números, e a soma dos valores é {acumulador}')