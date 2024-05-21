# Leia o nome e a média do aluno guardando a situação em um dicionário, no final mostra a estrutura
aluno = {}
aluno["nome"] = str(input("Digite o nome do aluno: "))
aluno["media"] = float(input(f"Digite a média de {aluno['nome']}: "))
if aluno["media"] <= 7:
    print(f"A situaçãod do aluno {aluno['nome']} é Reprovado.")
else:
    print(f"A situaçãod do aluno {aluno['nome']} é Aprovado.")
