# Faça um programa que leia número inteiro, pare quando for 999, mostre a quantidade de produtos e a suma entre eles
número = contagem = soma = 0
while True:
    número = int(input("Digite um número, [para parar digite 999]: "))
    if número == 999:
        break
    contagem += 1
    soma += número
print(f"Você digitou {contagem} números e a soma entre eles foi de {soma}!")
