# Desenvolva um programa que **leia** a **altura** e o peso de uma pessoa, calcule o **IMC** e mostre seu status de acordo com a tabela abaixo:
# < 18.5 | Abaixo do Peso
# < 25 | Peso Ideal
# < 30 | Sobrepeso
# < 40 | Obesidade
# >= 40 | Obesidade Mórbida
altura = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Seu IMC é {:.1f}, você está abaixo do peso.'.format(imc))
elif imc < 25:
    print('Seu IMC é {:.1f}, você está no peso ideal.'.format(imc))
elif imc < 30:
    print('Seu IMC é {:.1f}, você está com sobrepeso.'.format(imc))
elif imc < 40:
    print('Seu IMC é {:.1f}, você está com obesidade.'.format(imc))
else:
    print('Seu IMC é {:.1f}, você está com obesidade mórbida.'.format(imc))