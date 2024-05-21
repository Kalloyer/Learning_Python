# pessoas = {"Nome": "Kalleu", "Sexo": "M", "Idade": "22"}
# pessoas["Nome"] = "Jorge"  # Trocar os elementos desejados.
# pessoas["Peso"] = 85  # Adicionar os elementos desejados.
# print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.') #Para declarar é necessário as aspas duplas.
# print(pessoas.keys()) #São as chaves que irá exibir, como nome, sexo e idade.
# print(pessoas.values()) #Irá exibir os valores, como Kalleu, M, 22.
# print(pessoas.items()) # Mostra todos os elementos dentro do dicionário.
# del pessoas["Sexo"]  # Deleta o valor desejado
# for k, v in pessoas.items():
#     print(f"O {k} é {v}.")

# Dicionário dentro de uma lista
# brasil = []
# estado1 = {"UF": "Paraná", "Silga": "PR"}
# estado2 = {"UF": "São Paulo", "Sigla": "SP"}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil)
# print(brasil[0])
# print(brasil[0]["UF"])
# print(brasil[1])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado["UF"] = str(input("Unidade Federativa: "))
    estado["Sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())  # Tem que usar o copy, pois o fatiamento não funciona
for e in brasil:
    # for k, v in e.items():
    #     print(f"O campo {k} tem valor {v}.")
    for v in e.values():
        print(v, end=" ")
print()
