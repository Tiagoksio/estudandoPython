# Crie um programa que leia uma frase qualquer e diga se ela é um palidromo, desconsiderando os espaços. Exemplos de palíndromos: APOS A SOPA; A SACADA DA CASA; A TORRE DA DERROTA; O LOBO AMA O BOLO; ANOTARAM A DATA DA MARATONA.
frase = input('Informe uma frase: ')
fraseRegular = ''.join(frase.lower().split())
fraseInvertida = fraseRegular[::-1]
print("O texto '{}' é um Palindromo:".format(frase) if fraseRegular == fraseInvertida else "O texto '{}' não é um Palindromo:".format(frase))