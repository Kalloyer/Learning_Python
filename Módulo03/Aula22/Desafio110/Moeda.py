def aumentar(valor=0, taxa=0, formato=False):
    """-> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param valor: o preço desejado.
    :param taxa: qual a porcentamente do aumento.
    :param formato: True para formatado e False para não formatado.
    :return: o valor reajustado com ou sem formatação.
    """
    resposta = valor + (valor * taxa / 100)
    return resposta if formato is False else moeda(resposta)


def diminuir(valor=0, taxa=0, formato=False):
    resposta = valor - (valor * taxa / 100)
    return resposta if formato is False else moeda(resposta)


def dobro(valor=0, formato=False):
    resposta = valor * 2
    return resposta if formato is False else moeda(resposta)


def metade(valor=0, formato=False):
    resposta = valor / 2
    return resposta if formato is False else moeda(resposta)


def moeda(valor=0, moeda="R$"):
    return f"{moeda}{valor:.2f}".replace(".", ",")


def resumo(valor=0, taxaa=10, taxar=5):
    print(30 * "=")
    print(f'{'Resumo do valor'.center(30)}')
    print(30 * "=")
    print(f"Preço analisado: \t{moeda(valor)}")
    print(f"Dobro do preço: \t{dobro(valor, True)}")
    print(f"Metade do preço: \t{metade(valor, True)}")
    print(f"{taxaa}% de aumento: \t{aumentar(valor, taxaa, True)}")
    print(f"{taxar}% de redução: \t{diminuir(valor, taxar, True)}")
    print(30 * "=")
