# Crie um programa que leia vários números inteiros. No final, mostre a média entre todos os valores e qual foi o maior e o menor lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar.
contador = acumulador = num = media = 0

while True:
    contador += 1
    num = int(input(f'Informe o {contador}º número ou digite: '))
    acumulador += num
    if contador == 1:
        maior = num
        menor = num
    elif maior < num:
        maior = num
    elif menor > num:
        menor = num
    continuar = str(input('Deseja continuar? [S/N]').strip().upper())
    if continuar == 'N':
        break
print(f'\nForam informados "{contador}" números;\nA soma dos valores é "{acumulador}";\nO maior número informado foi "{maior}"\nO menor número informado foi "{menor}"\nA média dos valores é "{acumulador / contador}"')