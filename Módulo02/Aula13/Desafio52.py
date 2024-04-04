# Leia um numero inteiro e diga se ele é ou não um primo (divisiveis por 1 ou por ele mesmo)
num = int(input("Digite um número: "))
tot = 0
for c in range(1, num + 1, 1):
    if num % c == 0:
        print("\033[034m", end=" ")
        tot += 1
    else:
        print("\033[031m", end=" ")
    print("{}".format(c), end="")
print("\n\033[mO número {} foi divisível {} vezes!".format(num, tot))
if tot == 2:
    print("E por isso ele é um número primo!")
else:
    print("Ele não é um número primo!")
