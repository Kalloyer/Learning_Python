# Leia um numero inteiro e mostre os primeiros elementos de uma sequincia fibonnacci
print(14 * "=-=")
print(10 * "=", "Sequência Fibonnacci", 10 * "=")
print(14 * "=-=")
termo = int(input("Quantos termos você deseja mostrar? "))
termo1 = 0
termo2 = 1
print(42 * "~")
print("{} => {} => ".format(termo1, termo2), end="")
contador = 3
while contador <= termo:
    termo3 = termo1 + termo2
    print("=> {}".format(termo3), end=" ")
    termo1 = termo2
    termo2 = termo3
    contador += 1
print("=> Finalizado!")
