# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, descosidere-o;
somaPar = 0
for num in range(0, 6):
    numero = int(input('number {}: '.format(num + 1)))
    if numero % 2 == 0:
        somaPar += int(numero)
print('A soma dos pares é: {}'.format(somaPar)) 