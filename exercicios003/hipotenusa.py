import math
catOp = float(input('Informe o cateto oposto: '))
catAdj = float(input('Informe o cateto adjacente: '))
print('A hipotenusa é {:.2f}'.format(math.hypot(catOp, catAdj)))