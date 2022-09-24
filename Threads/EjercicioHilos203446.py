from ast import arg
import requests
import threading
import time 
import concurrent.futures
import mysql.connector
import pytube

threading_local = threading.local()

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    database = "apipc",
    user = "root",
    password = ""
)
cursor = mydb.cursor()

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)

def get_service(url):
    r = requests.get(url)
    write_db(r.json())
     
def write_db(data):
    
    for i in data['features']:
        cursor.execute("INSERT INTO sismos (place) VALUES ('" + i['properties']['place'] + "')")    
        mydb.commit()   
    
def get_users(x=0):

    response = requests.get('https://randomuser.me/api/')
    if response.status_code==200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)
            
def get_videos():
    yt = pytube.YouTube('https://www.youtube.com/watch?v=0bZ0hkiIKt0&ab_channel=shtinky')
    yt.streams.first().download("D:/Python/videos")


if __name__ == "__main__":
    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-03-05&limit=500'
    x = 0
    start_time = time.time()
    
    for i in range(0,500):
      th2 = threading.Thread(target=get_users, args=[x])  
      th2.start()
    
    th3 = threading.Thread(target=get_videos)
    th1 = threading.Thread(target=get_service, args=[url])
    th1.start()
    th3.start()
    
    end_time = time.time() - start_time
    print(end_time)
    
    



