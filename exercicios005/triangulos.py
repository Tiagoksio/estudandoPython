# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
segmento = []
while len(segmento) < 3:
    segmento.append(float(input('Informe o {}º segmento: '.format(len(segmento) + 1))))
if segmento[0] < segmento[1] + segmento[2] and segmento[1] < segmento[0] + segmento[2] and segmento[2] < segmento[1] + segmento[0]:
    print("Os segmentos {}, {} e {} formam um triângulo.".format(segmento[0], segmento[1], segmento[2]))
else:
    print("Os segmentos {}, {} e {} não formam um triângulo.".format(segmento[0], segmento[1], segmento[2]))