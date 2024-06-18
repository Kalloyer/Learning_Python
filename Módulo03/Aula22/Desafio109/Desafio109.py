# Crie um parâmetro adicional mostre de os valores serão ou não formatados
import Moeda

p = float(input("Digite o preço R$ "))
print(f"A metade de {p} é {Moeda.metade(p, False)}.")
print(f"O dobro de {p} é {Moeda.dobro(p, True)}.")
print(f"Aumentando 10%, temos {Moeda.aumentar(p, 10, False)}.")
print(f"Diminuindo 20% temos {Moeda.diminuir(p, 20, True)}.")
