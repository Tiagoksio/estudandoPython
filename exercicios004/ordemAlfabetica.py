nome = []
continuar = 's'
while continuar  != 'n':
    nome.append(input('Informe um nome: '))
    continuar = input('Deseja adicionar outro nome? [s/n]').lower()
nome = sorted(nome)
for item in nome:
    print(item)