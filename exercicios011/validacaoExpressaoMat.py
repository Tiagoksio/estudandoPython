# Crie um programa onde o usuário digite uma expressão matemática qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = input('Informe uma expressão numérica: ').strip()
if expressao.count('(') != expressao.count(')'):
    print('Expressão inválida')
else:
    expressao = eval(expressao)
    print(expressao)
'''
Outra forma de fazer:
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
'''