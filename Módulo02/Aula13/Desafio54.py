# Leia a idade de 7 pessoas e veja se é maior ou menor de idade
from datetime import date

ano = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nascimento = int(input("Em que ano a {}ª pessoal nasceu? ".format(pessoa)))
    idade = ano - nascimento
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(
    "Ao todo tivemos {} pessoas que são maiores de idade.\nE {} pessoas que são menores de idade.".format(
        totmaior, totmenor
    )
)
