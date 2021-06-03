opcao = int(input('Informe a conversão que deseja efetuar:\n1 - Celsius para Fahrenheit\n2 - Fahrenheit para Celsius\n'))
temp = float(input('Informe a Temperatura: '))
if opcao == 1:
    print('{} graus em Celsius equivale à {} graus em Fahrenheit'.format(temp, (temp / 5 * 9) - 32))
elif opcao == 2:
    print('{} graus em Fahrenheit equivale à {} graus em Celsius'.format(temp, (temp - 32) / 9 * 5))
else:
    print('Opção inválida')