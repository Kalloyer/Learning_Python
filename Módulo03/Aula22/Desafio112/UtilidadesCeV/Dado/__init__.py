def leiDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"\033[0;31mERRO: '{entrada}' é um preço inválido!\033[m")
        else:
            valido is True
            return float(entrada)
