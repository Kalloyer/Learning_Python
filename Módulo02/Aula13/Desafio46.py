#contagem regressiva 0 a 10 com uma pause de 1 segundo
from time import sleep
print('Contagem regressiva para queima de fogos.')
print(15 * '=+=')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('BOOM', 'PLAI', 'PLOFT', 'CABOOM')