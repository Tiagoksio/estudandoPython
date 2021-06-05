#Crie um programa que leia um número inteiro e mostre na tela se ele é **PAR** ou **IMPAR**;
num = int(input('Informe um número inteiro: '))
print('O número {} é PAR'.format(num) if num % 2 == 0 else "O número {} é IMPAR".format(num))