# Crie um programa que leia o nome de uma pessoa e diga se ele termina ou tem "SILVA" no nome;
nome = input('Informe um nome: ').lower()
if not 'silva' in nome:
    print('Nome não contém "silva"')
elif nome.split()[(len(nome.split()) - 1)] == 'silva':
    print('Nome possui e termina com "Silva"')
else:
    print('Nome possui "Silva", mas não termina com essa palavra')