# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as vogais.
palavras = ('pessoa', 'python', 'curso', 'mascara', 'schwarzenegger')
for palavra in palavras:
    print(f'\nNa palavra "{palavra.upper()}", temos as vogais: ', end='')
    for vogal in palavra:
        if vogal in 'aeiou':
            print(vogal, end=', ')
print('\n')