# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato;
jogador = dict()
gol = list()
jogador['nome'] = input('Informe o nome do jogador: ').strip()
jogador['partidas'] = int(input('Informe o número de partidas: '))
for jogo in range(0, jogador['partidas']):
    gol.append(int(input(f'Informe o número de gols da {jogo + 1}ª partida: ')))
jogador['gols'] = gol[:]
jogador['saldo'] = sum(jogador["gols"])
print(f'Nome do jogador: {jogador["nome"]}\nNº de Jogos: {jogador["partidas"]}')
for p, g in enumerate(jogador['gols']):
    print(f'Jogo {p + 1}: {g} gols')
print(f'Total: {jogador["saldo"]}')