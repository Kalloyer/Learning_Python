# Lista com nome e duas notas, no final mostre um boletim com a média de cada nota e permita mostrar a nota dos alunos individualmente
cadastro = []

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    cadastro.append([nome, [nota1, nota2], media])

    respota = str(input("Quer continuar? [S/N]: ")).lower().strip()[0]
    if respota == "n":
        break
print("=" * 60)
print(f'{"N.º":<5}{'Nome':<15}{'Média':>6}')
print("=" * 60)
for indice, aluno in enumerate(cadastro):
    print(f"{indice:<5}{aluno[0]:<15}{aluno[2]:>6.1f}")
while True:
    print("=" * 60)
    opcao = int(input("Motrar notas de qual aluno? (999 interrompe): "))
    if opcao == 999:
        print(f'{'Finalizando':=^60}')
        break
    if opcao <= len(cadastro) - 1:
        print(f"Notas de {cadastro[opcao][0]} são {cadastro[opcao][1]}.")
print(f'{'VOLTE SEMPRE':^15}')
