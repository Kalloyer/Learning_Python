# incio = int(input('Digite o inicio: '))
# fim = int(input('Digite o fim: '))
# passo = int(input('Digite o passo: '))
# for c in range(incio, fim+1, passo) :
#    print(c)
# print('FIM')

s = 0
for c in range(0, 3):
    n = int(input("Digite um valor: "))
    s += n
print("O somatório de todos os valores foi {}!".format(s))
