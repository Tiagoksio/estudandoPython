from random import choice
alunos = []
index = 0
while index < 4:
    alunos.append(input('Informe o nome do {}º aluno: '.format(index + 1)))
    index += 1
print('O aluno {} irá apagar o quadro'.format(choice(alunos)))