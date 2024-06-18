# Programa com a função notas, retorne um dicionário com as seguintes informações: quantidade, maior, menor, media e a situação do aluno, e a função docstring
def notas(*num, sit=False):
    """-> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas de alunos.
    :param sit: opcional, indicando se deve (True) ou não (False) adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    resposta = dict()
    resposta["Total"] = len(num)
    resposta["Maior"] = max(num)
    resposta["Menor"] = min(num)
    resposta["Media"] = sum(num) / len(num)
    if sit:
        if resposta["Media"] >= 7:
            resposta["Situação"] = "Aluno Aprovado"
        else:
            resposta["Situação"] = "Aluno Reprovado"
    return resposta


resp = notas(7, 7, 7, 6.97, sit=True)
print(resp)
help(notas)
