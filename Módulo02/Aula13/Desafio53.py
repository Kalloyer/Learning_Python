# Leia uma frase e descreve se ela é ou não um palindromo
frase = str(input("Digite um frase: ")).strip().upper()
palavra = frase.split()
inteiro = "".join(palavra)
contrario = ""
for letra in range(len(inteiro) - 1, -1, -1):
    contrario += inteiro[letra]
if contrario == inteiro:
    print("Essa frase é um palíndromo!")
else:
    print("Essa frase não é um palíndromo.")
