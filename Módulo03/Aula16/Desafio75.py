# Leia 4 valores, guarde os mesmos em uma tupla, mostra quantas vezes apareceu o valor 9, em que posição está o número 3, quais foram os pares
numero = (
    int(input("Digite um número: ")),
    int(input("Digite outro número: ")),
    int(input("Digite mais um número: ")),
    int(input("Digite o último número: ")),
)
print(f"Você digitou os valores {numero}.")
print(f"O valor 9 apareceu {numero.count(9)} vezes.")
if 3 in numero:
    print(f"O valor 3 aparece na {numero.index(3)+1}ª posição.")
else:
    print("O valor 3 não foi digitado em nenhum momento.")
print("Os valores pares digitados foram: ", end="")
for n in numero:
    if n % 2 == 0:
        print(n, end=" ")
