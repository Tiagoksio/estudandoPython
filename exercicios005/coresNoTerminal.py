# Cores no terminal com código ANSI: 
# '\033['style';'text';'background'm"Texto a colorir"\033[m'
style = {'none': 0, 'bold': 1, 'underline': 4, 'negative': 7}
text = {'branco': 30, 'vermelho': 31, 'verde': 32, 'amarelo': 33, 'azul': 34, 'majenta': 35, 'ciano': 36, 'cinza': 37}
background = {'branco': 40, 'vermelho': 41, 'verde': 42, 'amarelo': 43, 'azul': 44, 'majenta': 45, 'ciano': 46, 'cinza': 47}
configuracao = []
# Entrada da frase
frase =" ".join(input('Informe a frase que deseja colorir: ').split())
configuracao.append(input('Informe o estilo:\nnone - bold - underline - negative: ').lower())
configuracao.append(input('Informe a cor do texto:\nbranco - vermelho - verde - amarelo - azul - majenta - ciano - cinza: ').lower())
configuracao.append(input('Informe a cor de fundo:\nbranco - vermelho - verde - amarelo - azul - majenta - ciano - cinza: ').lower())

# Saída
print('\033[{};{};{}m{}\033[m'.format(style[configuracao[0]], text[configuracao[1]], background[configuracao[2]], frase))