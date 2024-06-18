# def titulo(til):  # Cria comandos personalizados
#     print(30 * "=")
#     print(til)
#     print(30 * "=")


# titulo(f"{"JOGO DO BICHO":^30}")
# titulo(f"{"JORGIN GAMEPLAYS":^30}")


# def soma(a, b):
#     s = a + b
#     print(f"A = {a} e B = {b}")
#     print(f"A soma de {a} + {b} é de {s}.")
#     print(30 * "=")


# soma(12, 1)
# soma(4, 5)
# soma(b=6, a=8)


# Parâmetro desempacotador
# def contador(*num):
#     # for valor in num:
#     #     print(f"{valor} ", end="")
#     # print("Finalizado")
#     tamanho = len(num)
#     print(f"Recebi os valores {num} e são ao todo {tamanho} números.")


# contador(0, 5)
# contador(1, 6, 7)
# contador(8, 9, 2, 3, 5, 4, 1)


# def dobra(lista):
#     posicao = 0
#     while posicao < len(lista):
#         lista[posicao] *= 2
#         posicao += 1


# valores = [5, 8, 4, 3, 9, 1]
# dobra(valores)
# print(valores)


def soma(*valores):
    soma = 0
    for numeros in valores:
        soma += numeros
    print(f"Somando os valores {valores}, temos a soma de {soma}.")


soma(12, 1)
soma(5, 2, 6)
soma(5, 2, 6, 1, 9, 10)
