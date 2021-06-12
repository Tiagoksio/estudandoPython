# Faça um programa que leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. Após finalizar o loop, o programa deve perguntar se o usuário deseja consultar mais termos e quantos;
contador = 0
mais = 1
razao = int(input('Informe a razão da PA: '))
termoInicial = int(input('Informe o primeiro termo: '))
qtdTermos = 10
while mais != 0:
    while contador < qtdTermos:
        contador += 1
        print('O {:2.0f}º termo é: {:2.0f}'.format(contador, termoInicial))
        termoInicial += razao        
    mais = int(input('Deseja consultar mais quantos termos?'))
    qtdTermos += mais