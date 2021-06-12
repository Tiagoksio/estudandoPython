# Crie um programa que leia dois valores e mostre um menu na tela: [1]Somar, [2]Multiplicar, [3]Maior, [4]Nova operação, [5]Sair. Seu programa deverá realizar a operação em cada caso;
def somar(num01, num02):
    return num01 + num02
def multiplicar(num01, num02):
    return num01 * num02
def maior(num01, num02):
    if num01 > num02:
        return num01
    else:
        return num02
def sair():
    print('Até mais!')
def novaOperacao():
    opcao = int(input('Informe a operação desejada: \n[1]Somar;\n[2]Multiplicar;\n[3]Maior;\n[4]Nova operação;\n[5]Sair\n:'))
    if opcao < 1 or opcao > 5:
        print('Opção inválida')
        novaOperacao()
    else:
        if opcao == 4:
            novaOperacao()
        elif opcao == 5:
            sair()
        else:
            num01 = int(input('Informe o primeiro número: '))
            num02 = int(input('Informe o primeiro segundo número: '))
            if opcao == 1:
                print(f'A soma de {num01} e {num02} é {somar(num01, num02)}')
                novaOperacao()
            elif opcao == 2:
                print(f'O produto de {num01} e {num02} é {multiplicar(num01, num02)}')
                novaOperacao()
            else:
                print(f'O maior número entre {num01} e {num02} é {maior(num01, num02)}')
                novaOperacao()
novaOperacao()