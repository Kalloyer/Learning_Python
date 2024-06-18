from Desafio115.Lib.Interface import *
from Desafio115.Lib.Arquivo import *
from time import sleep

arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver Pessoas Cadastradas',
                    'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:  # Lista o conteúdo de um arquivo
        lerArquivo(arquivo)
    elif resposta == 2:  # Opção para cadastrar uma pessoa
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        txterro('\033[1;31mErro!!! Digite um opção válida!\033[m')
    sleep(2)
