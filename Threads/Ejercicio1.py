from webbrowser import get
import requests
import threading
import time
from pytube import YouTube 

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

def get_services(x=0):
    print(f'Data input = {x}')
    time.sleep(0.5)
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)

if __name__ == '__main__':
    x=0
    for x in range(0,50):
        th1 = threading.Thread(target=get_services, args=[x])
        th1.start()
        #get_services()