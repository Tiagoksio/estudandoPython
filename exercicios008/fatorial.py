# Faça um programa que leia um número qualquer e mostre seu fatorial;
def fatorial(num):
    if num < 3:
        return num
    else:
        return num * fatorial(num - 1) 
num = int(input('Informe um número para calcular seu fatorial: '))
print(f'O fatorial de {num} é {fatorial(num)}')