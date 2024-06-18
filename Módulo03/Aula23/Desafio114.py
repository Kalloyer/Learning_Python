# Teste de site para verificar se está sendo acessível ou não
import urllib.error
import urllib.request

try:
    webURL = urllib.request.urlopen('https://youtu.be/8jAykqxIeqw')
except urllib.error.URLError:
    print('O site não está acessível no momento!')
else:
    print('Consegui acessar o site normalmente.')