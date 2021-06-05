# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar **80km/h**, mostre uma mensagem dizendo que ele foi multado. A multa vai custar **R$07,00** por cada km acima do limite;
velocidade = float(input('Informe a velocidade do carro: '))
print('Dirija com cuidado!' if velocidade <= 80 else 'Você foi multado em R${:.2f} por excesso de velocidade!'.format((velocidade - 80) * 7))