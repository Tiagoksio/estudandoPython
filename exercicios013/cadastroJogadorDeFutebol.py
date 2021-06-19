# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato;
jogador = dict()
gol = list()
time = list()
while True:
    jogador['nome'] = input('Informe o nome do jogador: ').strip()
    jogador['partidas'] = int(input('Informe o número de partidas: '))
    for jogo in range(0, jogador['partidas']):
        gol.append(int(input(f'Informe o número de gols da {jogo + 1}ª partida: ')))
    jogador['gols'] = gol[:]
    gol.clear()
    jogador['saldo'] = sum(jogador["gols"])
    time.append(jogador.copy())
    continuar = input('Deseja continuar[S/N]? ').strip().upper()
    if continuar == 'N':
        break
print('=' * 30)
print(f'={"TIME":^28}=')
print('=' * 30)
print(f'= {"Nº":<5}{"NOME":<7}{"GOLS":<7}{"JOGOS":<8}=')
for indice, atleta in enumerate(time):
    print(f'= {indice:<5}{atleta["nome"]:<9}{atleta["saldo"]:<8}{len(atleta["gols"]):<4} =')
print('=' * 30)
while True:
    continuar = int(input('Informe o número do jogador para consultar o aproveitamento por jogos ou digite "999" para sair: '))
    if continuar == 999:
        print('PROGRAMA ENCERRADO.')
        break
    elif continuar < 0 or continuar > len(time) - 1:
        print('Número inválido. ', end='')
    else:
        print(f'O jogador {time[continuar]["nome"]} teve o seguinte desempenho: ')
        for j, g in enumerate(time[continuar]["gols"]):
            print(f'Jogo {j + 1}: {g} gols')