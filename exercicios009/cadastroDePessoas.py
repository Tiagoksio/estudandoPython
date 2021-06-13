# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#    Quantas pessoas tem mais de 18 anos;
#    Quantos homens foram cadastrados;
#    Quantas mulheres tem menos de 20 anos.
maiores18 = homens = mulheresMenores20 = contador = 0
while True:
    contador += 1
    while True:
        idade = int(input(f'Informe a idade da {contador}ª pessoa: '))
        sexo = input(f'Informe o gênero da {contador}ª pessoa [F/M]: ').upper().strip()
        if idade > 0 and (sexo == 'F' or sexo == 'M'):
            break
        print('Dados inválidos. Verifique a idade e o sexo informado.')
    if idade >= 18:
        maiores18 += 1
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulheresMenores20 += 1
    continuar = input('Deseja continuar?[S/N]').strip().upper()
    if continuar == 'N':
        break
print(f'\nForam cadastradas {contador} pessoas;\nSão {maiores18} maiores de 18 anos;\nForam {homens} homens;\nForam {mulheresMenores20} mulheres menores de 20 anos.')