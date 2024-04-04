#Programa que leia o nome da cidade e diga se ela começa com Santo ou não
cidade = str(input('Qual o nome da cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')