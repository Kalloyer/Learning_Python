# Leia a função leiaInt(), só fazendo a validação de apenas um número
def leiaInt(msg):
    ok = False
    numero = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            numero = int(n)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número válido.\033[m")
        if ok:
            break
    return numero


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")
