# Leia a função chamado escreva() e mostre uma mensagem com o tamanho adaptável
def titulo(til):
    tamanho = len(til) + 4
    print(tamanho * "=")
    print(f"  {til}")
    print(tamanho * "=")


titulo("Roberval")
titulo("Jorgin Gameplays")
