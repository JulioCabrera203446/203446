from urllib import response
import requests
from threading import Thread
import time

urls = ['https://www.facebook.com', 'https://www.instagram.com', 'https://www.youtube.com', 'https://www.asdfgvf.com', 'https://www.reddit.com',
        'https://www.paypal.com', 'https://www.amazon.com', 'https://www.ejemplos.co','https://www.yahoo.com', 'https://www.wikipedia.org',
        'https://www.enter.co', 'https://www.0asdfsafg.com', 'https://www.rojadirecta.me', 'https://www.themeforest.net', 'https://www.qu8437f.com',
        'https://www.icefilms.info', 'https://madewsosdfmc.com', 'https://lsoengasdf134.com', 'https://www.10ejemplos.com', 'https://10ejemplos.com/category/gramática',
        'https://pinguinodigital.com/blog/ejemplos-sobre-que-es-una-url/', 'https://definicion.de/taekwondo/', 'https://cnnespanol.cnn.com/', 'https://www.tocacuatro.com/', 'https://www.09346283asgfsdgf.com/']

def verification(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            time.sleep(60)
            response = requests.head(url)
            if response.status_code == 200:
                print(f'El sitio {url} esta activo')
            else:
                print(f"El sitio {url} esta inactivo")
        else:
            print(f'El sitio {url} esta inactivo')
    except:
        print(f'El sitio {url} esta inactivo')

class Hilo(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        verification(self.url)

h1 = [Hilo(urls[0]), Hilo(urls[1]), Hilo(urls[2]), Hilo(urls[3]), Hilo(urls[4]), Hilo(urls[5]), Hilo(urls[6]), Hilo(urls[7]), Hilo(urls[8]), 
    Hilo(urls[9]), Hilo(urls[10]), Hilo(urls[11]), Hilo(urls[12]), Hilo(urls[13]), Hilo(urls[14]), Hilo(urls[15]), Hilo(urls[16]), Hilo(urls[17]), 
    Hilo(urls[18]), Hilo(urls[19]), Hilo(urls[20]), Hilo(urls[21]), Hilo(urls[22]), Hilo(urls[23]), Hilo(urls[24])]

for h in h1:
    h.start()
