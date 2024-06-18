# Leio a função maior e analise os valores passados qual é o maior
from time import sleep


def maior(*numeros):
    maior = contagem = 0
    print(40 * "=")
    print("Analisando os valores passados...")
    for valor in numeros:
        print(f"{valor}", end=" ", flush=True)
        sleep(0.3)
        if contagem == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contagem += 1
    print()
    print(f"Foram informados {len(numeros)} ao todo.")
    print(f"O maior valor informado foi {maior}.")


maior(2, 9, 4, 5, 3, 6, 8)
maior(5, 6, 7)
maior()
