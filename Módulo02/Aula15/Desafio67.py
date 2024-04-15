# Mostre a tabuada de vários números, um de cada vez e pare quando o valor digitado for negativo
número = 0
while True:
    número = int(input("Quer ver a tabuada de qual valor? "))
    print(20 * "==")
    if número < 0:
        break
    for contador in range(1, 11):
        print(f"{número} x {contador} = {número * contador}")
print("Programa encerrado, volte sempre!")
