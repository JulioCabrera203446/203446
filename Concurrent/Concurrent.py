import requests
import time
import psycopg2
import threading
import concurrent.futures
from pytube import YouTube

threading_local = threading.local()

conexiondb = psycopg2.connect(user='postgres', password='halojul100', host='localhost', port='5432', database='apipc')
cursor = conexiondb.cursor()

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)

def get_service(url):
    r = requests.get(url)
    write_db(r.json()) 

def get_randomU(x=0):
    response = requests.get('https://randomuser.me/api/?results=500')

    if response.status_code == 200:
        results = response.json().get('results')
        for name in results:
            
            write_db(name['name']['first'])


def write_db(data):
    for i in data['features']:
        cursor.execute("INSERT INTO nombres (name) VALUES('" + x + "')")
        conexiondb.commit()   

def download_videos():
    SAVE_PATH = "D:/Descargas"
  
    link=["https://www.youtube.com/watch?v=xWOoBJUqlbI",  
    "https://www.youtube.com/watch?v=xWOoBJUqlbI"
    ] 
  
    for i in link:  
        try:  
          
        
        
            yt = YouTube(i)  
        except:  
          
        
            print("Connection Error")  
      
    
        mp4files = yt.filter('mp4')  
    
        
        
        d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)  
        try:  
            
            d_video.download(SAVE_PATH)  
        except:  
            print("Some Error!")  
    print('Task Completed!')

if __name__ == "__main__":
    url = 'https://randomuser.me/api/?results=500'
    x = 0
    start_time = time.time()
    for i in range(0,500):
        th2= threading.Thread(target=get_randomU, args=[x])
        th2.start()

    th3 = threading.Thread(target=download_videos)
    th1 = threading.Thread(target=get_service, args=[url])
    th1.start()
    th3.start()

    end_time = time.time() - start_time
    print(end_time)
    conexiondb.close()