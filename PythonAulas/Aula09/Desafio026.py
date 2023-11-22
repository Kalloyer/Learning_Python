#Leia a frase e mostre quantas vezes aparece a letra A, em que posicao aparece a primeira vez e na ultima
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase\n'
      'Em que posição aparecea primeira vez: {}\n'
      'Em que posição aparece pela última vez: {}'
      .format(frase.count('A'), frase.find('A')+1, frase.rfind('A')+1))