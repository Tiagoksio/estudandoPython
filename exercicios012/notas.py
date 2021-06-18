# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
boletim = list()
while True:
    nome = input('Informe o nome: ')
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    continuar = input('Deseja continuar?[S/N] ').strip().upper()
    if continuar == 'N':
        break

print(f'=' * 30)
print('={:^28}='.format('BOLETIM'))
print(f'=' * 30)
print('{:<11}{:<14}{:<25}'.format('Nº', 'ALUNO', 'MÉDIA'))
for numero, aluno in enumerate(boletim):
    print('{:<11}{:<14}{:<25}'.format(numero, aluno[0], aluno[2]))
print('=' * 30)

while True:
    continuar = input('Deseja consultar as notas de algum aluno?[S/N]: ').strip().upper()
    if continuar == 'N':
        break
    else:
        numAlu = int(input('Informe o Nº do aluno que deseja consultar: '))
        if numAlu > len(boletim) - 1:
            print('Número inválido.')
        else:
            print('=' * 40)
            print('{:<8}{:<11}{:<13}{:<13}'.format('Nº', 'ALUNO', 'NOTA 01', 'NOTA 02'))
            print('=' * 40)
            print(f'{numAlu:<7} {boletim[numAlu][0]:<11} {boletim[numAlu][1][0]:<13} {boletim[numAlu][1][1]:<13}')
            print('=' * 40)