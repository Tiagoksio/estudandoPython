# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar, considerando a aposentadoria possível depois de 35 anos de contribuição;
from datetime import date
pessoa = dict()
pessoa['nome'] = input('Informe o nome: ').strip()
pessoa['idade'] = date.today().year - int(input('Informe o ano de nascimento: ').strip())
pessoa['ctps'] = int(input('Informe o número da CTPS ou "0", se não tiver: '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Informe o ano de contratação: '))
    pessoa['salario'] = float(input('Informe o valor do salário R$: '))
    if 35 - (date.today().year - pessoa['contratacao']) > 0:
        pessoa['aposentadoria'] = 'Estará liberada em ' + str(35 - (date.today().year - pessoa['contratacao'])) + ' anos'
    else:
        pessoa['aposentadoria'] = 'Já esta disponível'
for k, v in pessoa.items():
    print(f'{k}: {v}')


