# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre: 
#     1. Apenas os 5 primeiros colocados;
#     2. Os últimos 4 colocados da tabela;
#     3. Uma lista com os times em ordem alfabética;
#     4. Em que posição na tabela está o time da Chapecoense.
times = ('fortaleza', 'athletico-pr', 'flamengo', 'atletico-GO', 'atletico-mg', 'bragantino', 'fluminense', 'bahia', 'palmeiras', 'corinthians', 'ceara-sc', 'santos', 'internacional', 'juventude', 'cuiaba', 'sport recife', 'sao paulo', 'chapecoense', 'gremio', 'america-mg')

print(f'{"=" * 50}\n{"="}{" TABELA DO BRASILEIRÃO ":^48}{"="}\n{"=" * 50}')
while True:
    opcao = int(input(f'1 - Mostrar os 5 primeiros colocados\n2 - Os últimos 4 colocados\n3 - Times em ordem alfabética\n4 - Localizar time\n: '))
    if opcao > 0 and opcao <= 4:
        break
    print('Opção inválida\n')
if opcao == 1:
    for time in range(0, 5):
        print(f'{time + 1} - {times[time].title()}')
elif opcao == 2:
    for time in range(len(times), 16, -1):
        print(f'{time} - {times[time - 1].title()}')
elif opcao == 3:
    timesAlf = sorted(times)
    for pos, time in enumerate(timesAlf):
        print(f'{pos + 1:2.0f} - {time.title()}')
else:
    localizar = input('Informe o time que deseja localizar, sem acentos e com o espaço se houver: ').strip().lower()
    print(f'{times.index(localizar) + 1} - {localizar}')
print(f'{"=" * 50}\n{"="}{" FIM DA TABELA ":^48}{"="}\n{"=" * 50}')