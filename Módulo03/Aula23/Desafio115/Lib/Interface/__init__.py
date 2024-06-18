def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def linha(tamanho=42):
    return '\033[33m=\033[m' * tamanho


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def txterro(txt):
    print(linha())
    print(txt.center(52))


def menu(lista):
    cabeçalho('Menu Principal')
    contador = 1
    for item in lista:
        print(f'\033[36m{contador} - {item}\033[m')
        contador += 1
    print(linha())
    opção = leiaInt('\033[32mSua opção: \033[m')
    return opção
