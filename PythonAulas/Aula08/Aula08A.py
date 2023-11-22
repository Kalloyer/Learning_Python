#Math - Ciel (Arredondamento para cima) | Floor (Arredondamento para baixo) | Trunc (Eliminar da virgulara para frente) | Pow (Potência) | Sqrt (Raiz Quadrada)

import math
num = int(input('Digite um valor: '))
raiz = math.sqrt(num)
print('A raiz quadrade de {} é {}!'.format(num, math.ceil(raiz)))
print('A raiz quadrade de {} é {}!'.format(num, math.floor(raiz)))
