# Analise um expressão e veja se ela está com os parênteses abertos e fechados corretamente
expressao = str(input("Digite uma expressão: "))
lista = []
for simbolo in expressao:
    if simbolo == "(":
        lista.append("(")
    elif simbolo == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista) == 0:
    print("Sua expressão está válida.")
else:
    print("Sua expressão está inválida.")
