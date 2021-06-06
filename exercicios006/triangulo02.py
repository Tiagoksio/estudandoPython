# Faça um programa que leia os segmentos de um triângulo, informe se é possível formar um triângulo com os parâmentros passados e o tipo de triângulo: Equilátero, Isósceles ou Escaleno;
segmento = []
while len(segmento) < 3:
    segmento.append(float(input('Informe o {}º segmento: '.format(len(segmento) + 1))))

if segmento[0] < segmento[1] + segmento[2] and segmento[1] < segmento[0] + segmento[2] and segmento[2] < segmento[1] + segmento[0]:
    print("Os segmentos {}, {} e {} formam um triângulo".format(segmento[0], segmento[1], segmento[2]), end =' ' )
    if segmento[0] == segmento[1] and segmento[0] != segmento[2] or segmento[0] == segmento[2] and segmento[0] != segmento[1]:
        print('ISÓSCELES')
    elif segmento[0] == segmento[1] and segmento[0] == segmento[2]:
        print('EQUILÁTERO')
    else:
        print('ESCALENO')
else:
    print("Os segmentos {}, {} e {} não formam um triângulo.".format(segmento[0], segmento[1], segmento[2]))