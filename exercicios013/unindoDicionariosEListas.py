''' Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
   1. Quantas pessoas foram cadastradas;
   2. A média de idade do grupo;
   3. Uma lista com todas as mulheres;
   4. Uma lista com todas as pessoas com idade acima da média. '''
pessoas = list()
individuo = dict()
media = 0
while True:
    individuo['nome'] = input('Informe o nome: ').strip()
    while True:
        individuo['sexo'] = input('Informe o sexo[M/F]: ').strip().upper()
        if individuo['sexo'] in 'MF':
            break
        else:
            print('Valor inválido.')
    individuo['idade'] = int(input('Informe a idade: ').strip())
    media += individuo['idade']
    pessoas.append(individuo.copy())
    continuar = input('Deseja continuar[S/N]? ').strip().upper()
    if continuar == 'N':
        break
media /= len(pessoas)
print(f'\nForam cadastradas: {len(pessoas)} pessoas')
print(f'A média das idades é: {media:4.2f} anos')
print(f'As mulheres cadastradas foram:', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f' {p["nome"]}', end='')
print(f'\nAs pessoas acima da média das idades são:', end='')
for p in pessoas:
    if p['idade'] > media:
        print(f' {p["nome"]}', end='')
print()