lanche = (
    "Hambuerger",
    "Suco",
    "Pizza",
    "Sorvete",
)  # Pode ter dados de tipos diferentes
del lanche  # É possível deletar a tupla inteira
# print(lanche[3], lanche[-2], lanche[1:3], lanche[2:])
# Tuplas são imutáveis
# print(sorted(lanche)) # Mostra de forma organizada o solicitado
"""for comida in lanche:
    print(f"Eu vou comer {comida}!")
    if comida == "Suco":
        print(f"Eu vou tomar {lanche[1]}")"""
"""for comida in range(0, len(lanche)):
    print(lanche[comida], end=" -> ")
    print(comida)"""

# for posicao, comida in enumerate(lanche):
#    print(f"Irei comer {comida}, que está na {posicao}ª posição.")

a = (2, 1, 4)
b = (8, 9, 10, 3)
c = a + b
print(c)
print(c.count(10))  # Contagem de quantos números tem
print(c.index(8))  # Ver em qual posição está o número
