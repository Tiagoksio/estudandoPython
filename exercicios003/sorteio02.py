from random import shuffle
alunos = []
index = 0
while index < 4:
    alunos.append(input('Informe o nome do {}º aluno: '.format(index+ 1)))
    index += 1
shuffle(alunos)
index = 0
for nome in alunos:
    index += 1
    print('O {}ª aluno a apresentar o trabalho é: {}'.format(index, nome))