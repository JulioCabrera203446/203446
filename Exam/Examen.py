import threading
import time

palillo1 = threading.Lock()
palillo2 = threading.Lock()
palillo3 = threading.Lock()
palillo4 = threading.Lock()
palillo5 = threading.Lock()
palillo6 = threading.Lock()
palillo7 = threading.Lock()
palillo8 = threading.Lock()

class Persona():
    def __init__(self,left,right):
        self.left = left
        self.right = right
p1 = Persona(palillo8,palillo1)
p2 = Persona(palillo1,palillo2)
p3 = Persona(palillo2,palillo3)
p4 = Persona(palillo3,palillo4)
p5 = Persona(palillo4,palillo5)
p6 = Persona(palillo5,palillo6)
p7 = Persona(palillo6,palillo7)
p8 = Persona(palillo7,palillo8)

def run(p,name):
    f=p.left.acquire()
    if f:
        print (name, "Consigue los palillos de la izquierda")
    ff = p.right.acquire()
    if ff:
        print(name, "consigue los 2 palillos")
        print(name, "empieza a comer")
    time.sleep(3)
    p.right.release()
    p.left.release()

t1 = threading.Thread(target=run,args=(p1,"Persona1"))
t2 = threading.Thread(target=run,args=(p2,"Persona2"))
t3 = threading.Thread(target=run,args=(p3,"Persona3"))
t4 = threading.Thread(target=run,args=(p4,"Persona4"))
t5 = threading.Thread(target=run,args=(p5,"Persona5"))
t6 = threading.Thread(target=run,args=(p6,"Persona6"))
t7 = threading.Thread(target=run,args=(p7,"Persona7"))
t8 = threading.Thread(target=run,args=(p8,"Persona8"))

hilos = [t1, t2, t3, t4, t5, t6, t7, t8]

for h in  hilos:
    h.start()
