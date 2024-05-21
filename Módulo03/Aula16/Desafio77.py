# tupla com várias palavras sem acento e mostrar para cada palavra quais são suas vogais
palavras = (
    "Python",
    "Jorge",
    "Computador",
    "Caixa de Som",
    "Notebook",
    "Teclado",
    "Mouse",
    "Mousepad",
    "Controle",
    "Garrafinha",
    "Celular",
    "Smartphone",
)
for vogais in palavras:
    print(f"\nNa palavra {vogais.upper()} nós temos as vogais: ", end="")
    for letra in vogais:
        if letra.lower() in "aeiou":
            print(letra.upper(), end=" ")
