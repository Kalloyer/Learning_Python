# Leia todos os número mas pare quando o usuário digitar 999, no final mostra quantos números foram digitados e a soma deles menos o 999.
número = contagem = soma = 0
número = int(input("Digite um número, (use 999 se quiser parar): "))
while número < 999:
    soma += número
    contagem += 1
    número = int(input("Digite um número, (use 999 se quiser parar): "))
print(25 * "==")
print(
    "Foram digitados {} números.\nA soma dos números digitados foram de {}!".format(
        contagem, soma
    )
)
print(25 * "==")
