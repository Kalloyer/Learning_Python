# Programa tenha a função chamad área que receba a largura e comprimento o mostre a área do terreno
def terreno(largura, comprimento):
    soma = largura * comprimento
    print(f"A área de um terreno {largura} x {comprimento} é de {soma}m².")


print(f'{"Controle de Terrenos":^30}')
print(30 * "=")
largura = float(input("Largura(m): "))
comprimento = float(input("Comprimento(m): "))
terreno(largura, comprimento)
