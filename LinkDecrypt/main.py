# -*- coding: utf-8 -*-

import click
import base64, requests, os, re, sys
from urllib.parse import urlparse as parser
from bs4 import BeautifulSoup

def _crack(code):
        zeros = ''
        ones = ''
        for n, letter in enumerate(code):
            if n % 2 == 0:
                zeros += code[n]
            else:
                ones = code[n] + ones

        key = zeros + ones
        key = list(key)
        i = 0

        while i < len(key):
            if key[i].isdigit():
                for j in range(i+1,len(key)):
                    if key[j].isdigit():
                        u = int(key[i])^int(key[j])
                        if u < 10: 
                            key[i] = str(u)
                        i = j					
                        break
            i += 1
        
        key = ''.join(key)
        url = base64.b64decode(key)[16:-16].decode('utf-8')

        return url

def _decrypt(url):
    try:
        uri = parser(url).netloc
        print(uri)
        if uri == 'adf.ly':
            adfly = requests.get(url).text
            ysmm = re.findall(r"var ysmm = '(.*?)';", adfly)[0]
            decrypted_url = _crack(ysmm)

            return decrypted_url
        else:
            return 'Invalid URL!'
    except Exception as e:
        # ENABLE IF DEBUGGING!
        print("Exception! {}".format(e))
        exit()

@click.command()
@click.argument('URL', nargs=1)
@click.option('-f', '--file', is_flag=True, help='Input file.')
def main(url, file):
    if file:
        try:
            with open(url, 'r') as target, open('output.txt', 'w') as output:
                soup = BeautifulSoup(target, 'html.parser')
                
                if soup:
                    items = soup.select('a')
                else:
                    items = target.read().splitlines('\n')

                for item in items:
                    _url = item.get('href')
                    output.write("{} \n".format(_decrypt(_url)))

            print("¡Finalizado! Resultados guardados en output.txt")

        except Exception as e:
            print("Ocurrió un error: {}".format(e))    
    elif url:
        print(_decrypt(url))

    else:
        exit()

if __name__ == "__main__":
    main()