nome = str(input('Qual o seu nome? '))
if nome == 'Kalleu':
    print('Que nome maneirim meu padrin!')
elif nome == 'Kaio' or 'Joao':
    print('Que nome sem graça.')
else:
    print('Desculpa esse nome não consta no meu sistema...')
print('Tenha um dia bom, \033[36m{}\033[m!!'.format(nome))