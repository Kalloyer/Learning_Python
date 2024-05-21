# Lei nome, ano de nasciomento (mas guarde a idade), carteira de trabalho, se for =!, ano de contratação e o salário, calcule a idade e com quantos anos a pessoa irá se aposentar
from datetime import datetime

dados = {}
dados["Nome"] = str(input("Nome: "))
nascimento = int(input("Ano de Nascimento: "))
dados["Idade"] = datetime.now().year - nascimento
dados["CTPS"] = int(input("Nº Carteira de Trabalho (0 não tem): "))
if dados["CTPS"] != 0:
    dados["Contratação"] = int(input("Ano de Contratação: "))
    dados["Salário"] = float(input("Salário: R$ "))
    dados["Aposentadoria"] = dados["Idade"] + (
        (dados["Contratação"] + 35) - datetime.now().year
    )
print(40 * "=")
for chave, valor in dados.items():
    print(f"• {chave} tem o valor {valor}.")
