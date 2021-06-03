opcao = int(input('Informe a operação desejada:\n1 - Descobrir o percentual acrescentado ou deduzido de um certo valor\n2 - Acrescentar ou deduzir um percentual de um certo valor\n3 - Descobrir o valor total a partir de um valor parcial e seu percentual equivalente\n'))
if opcao == 1:
    n1 = float(input('Informe o valor inicial: '))
    n2 = float(input('Informe o valor com os acrescimos ou deduções: '))
    print('A diferença percentual entre {} e {} é de {}%'.format(n1, n2, (n2-n1) / n1 * 100))
elif opcao == 2:
    n1 = float(input('Informe o valor inicial: '))
    n2 = float(input('Informe o percentual sem o "%", que deseja aplicar: '))
    print('O número {} com uma alteração de {}%, fica {}'.format(n1, n2, n2 / 100 * n1 + n1))
elif opcao == 3:
    n1 = float(input('Informe o valor parcial: '))
    n2 = float(input('Informe o percentual do total que esse valor equivale: '))
    print('O número {} equivale à {}%, de {}'.format(n1, n2, n2 * 100 / n1))
else:
    print('Opção inválida')