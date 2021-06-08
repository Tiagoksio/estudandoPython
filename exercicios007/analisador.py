# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#  A média da idade do grupo;
#  Qual é o nome do homem mais velho;
#  Quantas mulheres tem menos de 20 anos.
pessoas = []
idadeHoMaisVelho = 0
homMaisVelho = ''
qtdMulSub20 = 0
media = 0
def cadastrar():
    p = {}
    p['nome'] = input('Informe o nome: ')
    p['idade'] = int(input('Informe a idade: '))
    p['sexo'] = input('Informe o sexo [m/f]: ').lower()
    return p

for cadastro in range(0,5):
    print('\nCadastrar a {}ª pessoa\n'.format(cadastro + 1))
    pessoas.append(cadastrar())

    if pessoas[cadastro]['sexo'] == 'm' and pessoas[cadastro]['idade'] > idadeHoMaisVelho:
        homMaisVelho = pessoas[cadastro]['nome']
        idadeHoMaisVelho = pessoas[cadastro]['idade']
    if pessoas[cadastro]['sexo'] == 'f' and pessoas[cadastro]['idade'] < 20:
        qtdMulSub20 += 1
    media += pessoas[cadastro]['idade']
media /= 4

print('\nA média da idade do grupo é: {}'.format(media))
print('O homem mais velho é o {} com {} anos'.format(homMaisVelho, idadeHoMaisVelho))
print('A quantidade de mulhers menores de 20 anos é: {}'.format(qtdMulSub20))