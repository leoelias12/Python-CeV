import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('O site não está acessivel no momento')
else:
    print('o site está acessivel')

print(site.read())  # imprime o código do site
