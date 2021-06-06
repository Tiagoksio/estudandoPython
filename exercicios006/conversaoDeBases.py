# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a **base de conversão**:
# - **1** => para **binário**;
# - **2** => para **octal**;
# - **3** => para **hexadecimal**;
print('{:=^30}'.format(' BASES NUMÉRICAS '))
opcao = int(input('1 - BINÁRIO\n2 - OCTAL\n3 - HEXADECIMAL\nSelecione a opção: '))
num = int(input('Informe o número: '))
if opcao == 1:
    print('O número {} em base BINÁRIA é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em base OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em base HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVÁLIDA')