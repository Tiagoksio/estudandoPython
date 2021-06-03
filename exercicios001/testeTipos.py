#Testes de tipos
n1 = input('Digite um algo: ')
#podemos utilizar as máscaras para uma escrita semelhante a linguagem c, sem a necessidade de ficar concatenando strings
print('O valor informado {} é do tipo {}\n Numeral: {}\n Caractere: {}\n AlphaNumerico: {}\n Letras maiúsculas: {}\n Letras minúsculas: {}\n' .format(n1, type(n1), n1.isnumeric(), n1.isalpha(), n1.isalnum(), n1.isupper(), n1.islower()))