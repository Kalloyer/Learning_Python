# Programa de fatorial com a função fatorial que o primeiro parâmetro seja calcular somente o valor e o segundo que mostre o calculo através do show (opcional)


def fatorial(numero, show=False):
    """Calcula o fatorial de um número:

    Args:
        numero (_type_): O número a ser calculado.
        show (bool, optional): Mostrar ou não a conta. Padrão é False.

    Returns:
        _type_: O valor do Fatorial de um número.
    """
    print(30 * "=")
    f = 1
    for contagem in range(numero, 0, -1):
        if show is True:
            print(f"{contagem}", end="")
            print(" x " if numero > 1 else " = ", end="")
        f *= contagem
        numero -= 1
    return f


print(fatorial(5, show=True))
help(fatorial)
