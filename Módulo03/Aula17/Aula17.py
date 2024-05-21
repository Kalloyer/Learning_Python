"""num = [2, 3, 7, 10]
num[0] = 8
num.append(7)  # Acrescentar um número da lista
# num.sort()  # Organizar a lista
num.sort(reverse=True)  # Organizar de trás para frente
num.insert(2, 0)  # Inseri um valor na posição desejada
# num.pop()  # Sem parametro ele elimina o último número
# num.remove(7)  # Ele busca a primeira ocorrencia na lista para poder remover
print(num)
if 12 in num:
    num.remove(12)
else:
    print("Não achei o número 12 na lista.")
print(f"Essa lista tem {len(num)} elementos!")  # Retorna a quantidade de elementos"""

"""valores = []
# valores.append(1)
# valores.append(5)
# valores.append(3)
for contagem in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for posicao, valor in enumerate(valores):
    print(f"Na posição {posicao + 1}, encontreio o valor {valor}.")
print(15 * "-=-")
print(f"{"Cabo a lista":^45}")"""

a = [2, 3, 4, 7]
# b = a # Ele uni as duas listas, uma ligação
b = a[:]  # Ele faz um cópia da lista
b[2] = 8
print(f"Lista A = {a}. \nLista B = {b}.")
