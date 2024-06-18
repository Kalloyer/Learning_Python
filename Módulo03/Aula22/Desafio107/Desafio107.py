# Crie o modulo moeda que tenha as funções aumentar, diminuir, dobre e metade e importe elas
from Desafio107 import Moeda

p = float(input("Digite o preço R$ "))
print(f"A metade de {p} é {Moeda.metade(p):.2f}.")
print(f"O dobro de {p} é {Moeda.dobro(p):.2f}.")
print(f"Aumentando 10%, temos {Moeda.aumentar(p, 10):.2f}.")
print(f"Diminuindo 20% temos {Moeda.diminuir(p, 20):.2f}.")
