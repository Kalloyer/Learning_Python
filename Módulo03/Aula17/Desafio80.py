# Crie um programa que inseri os valores digitado em ordem numérica sem usar o sorte e mostre a lista
lista = []
for contagem in range(0, 5):
    valor = int(input("Digite um valor: "))
    if contagem == 0 or valor > lista[-1]:
        lista.append(valor)
        print("Adicionado ao final da lista.")
    else:
        posicao = 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                print(f"Adicionado na {posicao+1}ª posição.")
                break
            posicao += 1
print("==" * 30)
print(f"Os valores digitado em ordem foram: {lista}.")
