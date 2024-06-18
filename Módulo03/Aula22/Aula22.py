from Pacotes import Números

num = int(input("Digite uma valor: "))
fat = Números.fatorial(num)
print(f"O fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {Números.dobro(num)}.")
print(f"O triplo de {num} é {Números.triplo(num)}.")
