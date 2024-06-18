# Leia uma lista chamaada numeros e duas funções sorteia() e somapar(). A primeira sorteia 5 num e coloque dentro da lista ja a segunda soma os valores pares da lista
from random import randint
from time import sleep


def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end="")
    for contagem in range(0, 5):
        numero = randint(0, 10)
        lista.append(numero)
        print(f"{numero}", end=" ", flush=True)
        sleep(0.3)
    print()


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {lista}, temos {soma}!")
    print(f"{"FINALIZADO":=^60}")


numeros = []
sorteia(numeros)
somapar(numeros)
