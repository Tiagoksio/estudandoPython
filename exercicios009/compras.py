# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#     Qual é o total gasto na compra.
#     Quantos produtos custam mais de R$1000;
#     Qual é o nome do produto mais barato.
acumulador = acuMais1000 = prodBarValor = 0
prodBaratoNome = ''

while True:
    produtoNome = input('Informe o nome do produto: ').strip()
    produtoValor = float(input('Informe o valor do produto: '))
    if produtoValor > 1000:
        acuMais1000 += 1
    if prodBarValor == 0 or produtoValor < prodBarValor:
        prodBarValor = produtoValor
        prodBaratoNome = produtoNome
    acumulador += produtoValor
    continuar = input('Deseja continuar?[S/N]').strip().upper()
    if continuar == 'N':
        break
print(f'\nO total da compra vai ser R${acumulador:.2f}\n{acuMais1000} produtos custaram mais de R$1000,00\nO produto mais barato foi "{prodBaratoNome} no valor de R${prodBarValor:.2f}"')
    
