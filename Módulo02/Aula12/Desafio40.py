#Calcule a nota de um aluno, mostrando a média - Abaixo de 5.0 Reprocado | 5.0-6.9 Recuperação | 7.0 + Aprovado
nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
soma = (nota1 + nota2) / 2
if soma <= 50:
    print('Você foi reprovado, ficou com a média a baixo de 5.0! \nSua nota final foi de {:.2f}!!!'.format(soma))
elif soma >= 50 <= 69:
    print('Você ficou de recuperação, sua nota final foi de {:.2f}!!!'.format(soma))
else:
    print('Você foi aprovado, ficou com a média de {:.2f}!!!'.format(soma))