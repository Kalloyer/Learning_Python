# help(print)  # Ajuda interativa


# Docstring
# def contador(i, f, p):
#     # Documento da função:
#     """
#     -> Far uma contagem e mostra na tela.
#     :param i: inicio da contagem
#     :param f: final da contagem
#     :param p: passo da contagem
#     return: sem retorno
#     """
#     contador = i
#     while contador <= f:
#         print(f"{contador}", end=" ")
#         contador += p
#     print("FIM")


# contador(2, 10, 2)
# help(contador)

# Parâmetros Opcionais
# def somar(a=0, b=0, c=0):
#     """
#     -> Far a soma dos três valores e mostre na tela.
#     :param a: primeiro valor
#     :param b: segundo valor
#     :param c: terceiro valor
#     Se não estiver inserido nenhum valor o mesmo será considerado como 0.
#     """
#     s = a + b + c
#     print(f"A soma dos valores é de {s}!")


# somar(0, 1, 3)
# somar(5, 6)
# somar(a=100, c=6)
# somar()

# Escopo de Variáveis
# def teste(b):
#     global a  # Varivael global (vale para todo o programa)
#     a = 8
#     b += 4
#     c = 2
#     print(f"A dentro vale {a}.")
#     print(f"B dentro vale {b}.")
#     print(f"C dentro vale {c}.")


# a = 5
# teste(a)
# print(f"A fora vale {a}.")


# Retornando Variáveis
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s  # Possível dar retornos personalizados para a função.


s1 = somar(0, 1, 3)
s2 = somar(5, 6)
s3 = somar(a=100, c=6)
s4 = somar()
print(f"As somas deram {s1}, {s2}, {s3} e {s4}.")
