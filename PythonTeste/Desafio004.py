# Faça um programa que leia algo sobre o teclado e mostre o seu tipo e todas as informações possíveis!

n = input('Digital Algo: ')
print(type(n), n.isalnum(), n.isalpha(), n.isdecimal(), n.isdigit(), n.islower())