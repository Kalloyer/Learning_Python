# Programa que tenha uma funcao chamada voto, com o parametro de ano do nascimento, retornando o valor literal, mostre se o voto é negado, opcional e obrigatório
def voto(ano):
    from datetime import date

    anoatual = date.today().year
    idade = anoatual - ano
    if 18 <= idade < 65:
        return f"Com {idade} anos: Voto Obrigatório."
    elif idade < 18 or idade >= 65:
        return f"Com {idade} anos: Voto Opcional."
    else:
        return f"Com {idade} anos: Voto Não Obrigatório."


nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
