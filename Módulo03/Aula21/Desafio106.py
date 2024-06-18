# Mini sistema que utiliza o interactive help, o usuário vai digitar o comando e o manual vai aparecer, assim que digitar FIM irá encerrar.
from time import sleep

cores = (
    "\033[7;49;37m",  # Fundo Branco -> 0
    "\033[7;49;32m",  # Fundo verde -> 1
    "\033[49;96m",  # Escrite Azul Claro -> 2
    "\033[7;49;91m",  # Fundo Vermelho -> 3
)


def ajuda(com):
    titulo(f"Acessando o manual do comando {com}", 2)
    print(cores[0], end="")
    help(com)
    print(cores[0], end="")
    sleep(2)


def titulo(msg, cor=0):
    print(cores[cor], end="")
    tamanho = len(msg) + 4
    print("=" * tamanho)
    print(f"  {msg}  ")
    print("=" * tamanho)
    print(cores[0], end="")
    sleep(1)


while True:
    titulo("Sistema de Ajuda", 1)
    comando = str(input("Função ou Blibioteca > "))
    if comando.lower().strip() == "fim":
        break
    else:
        ajuda(comando)
titulo("Até Logo", 3)
