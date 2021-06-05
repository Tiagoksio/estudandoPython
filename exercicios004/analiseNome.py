nome = " ".join(input('Informe o nome completo para análise: ').upper().split())
print("""Nome com letras maiúsculas: {};
Nº de letras sem os espaços: {}
Nº de letras do primeiro nome: {}
Primeiro e o último nome: {}, {}""".format(nome.upper(), len(nome) - len(nome.split()) + 1, len(nome.split()[0]), nome.split()[0].capitalize(), nome.split()[len(nome.split()) - 1].capitalize()))
