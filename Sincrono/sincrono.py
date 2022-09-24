import requests
import time
import psycopg2

conexion = psycopg2.connect(user='postgres', password='halojul100', host='localhost', port='5432', database='api_pc')
cursor = conexion.cursor()

def get_name():
    response = requests.get('https://randomuser.me/api/?results=2000')

    if response.status_code == 200:
        results = response.json().get('results')
        for name in results:  
            write_db(name['name']['first'])
            
def write_db(x):
    cursor.execute("INSERT INTO nombres(name) VALUES('"+x+"')")
    conexion.commit()   

if __name__ == "__main__":
    start_time = time.time()
    get_name()
    end_time = time.time()
    print(end_time - start_time)
    conexion.close()