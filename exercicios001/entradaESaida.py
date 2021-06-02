# Conceitos básicos de entrada e saída, além de tentar entender como funciona o parse, funções e estrutura if em python
def entrada():
    nome = input("Qual é o seu nome? \n")
    print('Olá, {}! ' .format(nome) + 'Qual é a sua data de nascimento?')
def nascimento():
    dia = input('Dia:')
    mes = input('Mês:')
    ano = input('Ano:')
    dataCorreto = input('Você faz nasceu no dia ' + dia + ' de ' + mes + ' de ' + ano + ', correto?[s/n]')
    if (dataCorreto == 's'):
        numero01 = input('informe um número: ')
        numero02 = input('informe outro número: ')
        soma = int(numero01) + int(numero02)
        print('A soma entre ' + numero01 + ' e ' + numero02 + ' é ' + str(soma))
    else:
        nascimento()
entrada()
nascimento()