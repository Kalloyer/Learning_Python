# Cria uma listagem de produtos e seus preços
lista = (
    "Pão",
    13.89,
    "Leite",
    4,
    "Farinha",
    19.98,
    "Presunto",
    2.53,
    "Mussarela",
    3.65,
    "Coca-Cola",
    9.70,
    "Macarrão",
    6.49,
    "Doritos",
    9.99,
    "Bis",
    5.99,
    "Café",
    15.38,
)
print("=" * 40)
print(f"{'Lista de Compras':^40}")
print("=" * 40)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f"{lista[item]:.<32}", end="")
    elif item % 2 == 1:
        print(f"R$ {lista[item]:>5.2f}")
print("=" * 40)
