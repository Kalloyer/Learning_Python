#Crie um programa que jogue jakenpô
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('{:=^40}'.format('Jakenpô'))
print('''Ecolha entre:
      [0] Pedra
      [1] Papel
      [2] Tesoura''')
jogador = int(input('Escolha a sua jogada: '))
print('==' * 15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('==' * 15)
if computador == 0: #Computer jogou Pedra
    if jogador == 0:
        print('Empatou')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Jogador Perde')
    else:
        print('Jogada Inválida!!!')
elif computador == 1: #Computer jogou Papel
    if jogador == 0:
        print('Jogador Perde')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('Jogada Inválida!!!')
else: #Computer jogou Tesoura
    if jogador == 0:
        print('Jogador Vence')
    elif jogador == 1:
        print('Jogador Perde')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Inválida!!!')
print('==' * 15)