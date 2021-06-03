class Aluno:
    def __init__(self, nome, nota01, nota02):
        self.nome = nome
        self.nota01 = nota01
        self.nota02 = nota02
        self.media = (nota01 + nota02) / 2
    pass

alunos = []

def entrada():
    nome = input('Informe o seu nome: ')
    nota01 = float(input('Informe sua primeira nota: '))
    nota02 = float(input('Informe sua segunda nota: '))
    alunoCadastrado = Aluno (nome, nota01, nota02)
    return alunoCadastrado
    
def imprimirResultado():
    print('{:=^60}'.format('NOTAS'))
    print('{:<25}{:<10}{:>10}{:>15}'.format('ALUNO', 'NOTA 01', 'NOTA 02', 'MÉDIA'))
    for alu in alunos:
        print('{:<25}{:<10}{:>10}{:>15}'.format(alu.nome, alu.nota01, alu.nota02, alu.media))
    print('{:=^60}'.format('FIM'))

def iniciar():
    mostrar = input("Deseja visualizar os alunos cadastrados?[s/n]")
    if (mostrar == 's'):
        imprimirResultado()
    else:
        alunos.append(entrada())
        iniciar()
iniciar()