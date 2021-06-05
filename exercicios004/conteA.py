'''Faça um programa que leia uma frase pelo teclado e mostre:
   Quantas vezes aparece a letra "A";
   Em que posição ela aparece pela primeira vez;
   Em que posição ela aparece pela última vez.'''
frase = " ".join(input('Informe uma frase: ').lower().split())
print('''A frase: "{}"...
Possui {} letras "A";
A primeira letra "A" aparece na {}ª posição;
A última letra "A" aparece na {}ª posição.'''.format(frase.capitalize(), frase.count("a"), frase.find("a") + 1, frase.rfind("a") + 1))