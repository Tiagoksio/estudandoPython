num = int(input('Informe o número que deseja saber a tabuada: '))
multiplica = 0
while  multiplica <= 10:
    print('{} x {:2} = {}'.format(num, multiplica, num * multiplica))
    multiplica += 1
