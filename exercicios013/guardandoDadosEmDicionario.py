# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário, se está aprovado ou reprovado. No final, mostre o conteúdo da estrutura na tela;
aluno = {'nome': '', 'media': '', 'situacao': ''}
aluno['nome'] = input('Informe o nome do aluno: ')
aluno['media'] = float(input('Informe a média: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
for key, value in aluno.items():
    print(f'{key.capitalize()}: {value}')