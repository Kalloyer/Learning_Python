# Crie uma função adicional chamado moeda que mostre os valores formatados
import Moeda

p = float(input("Digite o preço R$ "))
print(f"A metade de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.metade(p))}.")
print(f"O dobro de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.dobro(p))}.")
print(f"Aumentando 10%, temos {Moeda.moeda(Moeda.aumentar(p, 10))}.")
print(f"Diminuindo 20% temos {Moeda.moeda(Moeda.diminuir(p, 20))}.")
