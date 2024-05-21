# Leia vários valores, se já estiver na lista não é para cadastrar mais, depois mostre tudo em ordem crescente
valores = []
while True:
    numero = int(input("Digite um valor para cadastrá-lo: "))
    if numero not in valores:
        valores.append(numero)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor já cadastrado...")
    resposta = str(input("Quer continuar? [S/N]: ")).lower().strip()[0]
    if resposta == "n":
        break
print(30 * "=")
print("Programa Finalizado")
