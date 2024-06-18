# Leia a função leiaInt(), só fazendo a validação de apenas um número
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[3;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[3;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n
        

n1 = leiaInt("Digite um número inteiro: ")
n2 = leiaFloat('Digite um número real: ')
print(40 * '=')
print(f"O valor inteiro digitado foi {n1}.\nO valor real digitado foi {n2}.")
