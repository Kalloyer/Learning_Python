# Refazer o desafio 09 mostrando a tabuada com o número que o usuário escolher utilizando o laço for
numero = int(input("Digite um número: "))
print("-=-" * 6, "TÁBUADA", "-=-" * 6)
print("-=-" * 15)
for c in range(1, 11):
    print(c * numero)
print("-=-" * 15)
