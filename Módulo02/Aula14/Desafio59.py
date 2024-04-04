# Leia dois números e mostre a tela as opções e faça os cáculos
from time import sleep

número1 = int(input("Digite o 1º valor: "))
número2 = int(input("Digite o 2º valor: "))
opcao = 0
while opcao != 5:
    print("""Escolha uma das opções abaixo:
            [1] Soma
            [2] Multiplicação
            [3] Maior
            [4] Novos Números
            [5] Sair""")
    opcao = int(input("Escolha uma das opções acima: "))
    if opcao == 1:
        print(
            "Os soma dos valores digitados {} e {} é de {}.".format(
                número1, número2, número1 + número2
            )
        )
    elif opcao == 2:
        print(
            "A multiplicação dos valores digitados {} e {} é de {}.".format(
                número1, número2, número1 * número2
            )
        )
    elif opcao == 3:
        if número1 > número2:
            print("O primeiro número digitado é maior que o segundo!")
        if número2 > número1:
            print("O segundo número digitado é maior que o primeiro!")
    elif opcao == 4:
        print(15 * "=-=")
        print("Informe os números novamente:")
        número1 = int(input("Digite o 1º valor: "))
        número2 = int(input("Digite o 2º valor: "))
    elif opcao == 5:
        print(40 * "-")
        print("Você saiu do programa, volte sempre!")
    else:
        print("Opção inválida.")
    sleep(2)
    print(20 * "-=-")
