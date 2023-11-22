#escreva um programa que pense em um numero de 0 a 5 e faça o usuário tentar descobrir qual o número escolhido, o programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep
print('Vou pensar em um número de 0 a 5 tente adivinhar!!!\nProcessando...')
sleep(3)
print('-=-' * 25)
numero = int(input('Digite um número de 0 a 5: '))
lista = randint(0,5)
print('Você venceu, PARABÉNS!' if lista == numero else 'Você perdeu, tente novamente!')