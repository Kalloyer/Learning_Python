# Tenha uma função chamada contador() com tres parametros, inicio, fim e passo
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print(40 * "=")
    print(f"Contagem de {i} até {f} de {p} em {p}.")
    sleep(1)

    if i < f:
        contagem = i
        while contagem <= f:
            print(
                f"{contagem}", end=" ", flush=True
            )  # Utilizar o Flush para pular o buffer de tela
            sleep(0.5)
            contagem += p
        print("FIM")
    else:
        contagem = i
        while contagem >= f:
            print(f"{contagem}", end=" ", flush=True)
            sleep(0.5)
            contagem -= p
        print("FIM")


contador(1, 10, 1)
contador(10, 0, 2)
print(40 * "=")
print("Agora é a sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
