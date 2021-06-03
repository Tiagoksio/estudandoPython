largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
litros = largura * altura / 2
print('Para pintar uma parede de {:.2f}m², serão necessários {} litros de tinta'.format(largura * altura, litros))
