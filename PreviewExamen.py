import time
import requests

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

for url in urls:
    verification(url)
    