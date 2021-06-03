n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
# adição
print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
# subtração
print('O número {} menos {} é {}'.format(n1, n2, n1-n2))
#Multiplicação
print('O produto entre {} e {} é {}'.format(n1, n2, n1*n2))
#divisão
print('O número {} dividido por {} é {:.3f}'.format(n1, n2, n1/n2))
#potenciação
print('O número {} elevado a {} é {}'.format(n1, n2, n1**n2))
#raiz
print('A raíz {} de {} é {:.4f}'.format(n2, n1, n1**(1/n2)))
#divisão inteira
print('O número {} divido inteiramente por {} é {}'.format(n1, n2, n1//n2))
#resto

print('O resto da divisão de {} por {} é {}'.format(n1, n2, n1%n2))
# segue a ordem de precedência: (), **, divisões e multiplicações, soma e subtração.
# podemos exercutar esses operadores com strings
nome = input('Qual é o seu nome? ')
print('Nome centralizado entre simbolos: {:=^20}'.format(nome))
print('Nome alinhado a direita com 20 espaços: {:>20}'.format(nome))
print('Nome alinhado a esquerda: {:<20}'.format(nome), end= 'fim\n')
print('Nome escrito várias vezes: {}'.format(nome * 5))