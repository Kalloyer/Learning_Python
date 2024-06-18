def aumentar(valor=0, taxa=0, formato=False):
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
