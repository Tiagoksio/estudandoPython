from math import radians, sin, cos, tan
angulo = float(input('Informe o ângulo do triângulo: '))
print('As razões trigonométricas do ângulo {}º são:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))