número = soma = 0
while True:
    número = int(input("Digite um número: "))
    if número == 999:
        break
    soma += número
# print("A soma dos valores digitados é de {}!".format(soma))
print(f"A soma vale {soma}!")
