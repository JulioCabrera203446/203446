#Julio Antonio Cabrera Yañez - 203446

import threading
import random
import queue
import time

capacidad = queue.Queue(maxsize=20)
meseros = queue.Queue(maxsize=2)
cocineros = queue.Queue(maxsize=2)
clientes_pause = queue.Queue()
reservaciones = queue.Queue(maxsize=4) 
reservaciones_pause = queue.Queue()
ordenes = queue.Queue()
ordenes_finalizadas = queue.Queue()

lock = threading.Lock()

class Cliente(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.monitor = threading.Condition()

    def comer(self):
        while True:
            with self.monitor:
                if not ordenes_finalizadas.empty():
                    id_cliente = capacidad.get()
                    print(f'Cliente {id_cliente} esta comiendo su platillo')
                    time.sleep(random.randint(4, 7))
                    print(f'Cliente {id_cliente} termina de comer y se retira')
                    ordenes.get()
                    self.monitor.notify()

    def run(self):
        self.comer()

class Reservacion(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.monitor = threading.Condition()

    def reservar(self):
        while True:
            with self.monitor:
                if not reservaciones.full():
                    reservaciones.put(self.id)
                    print(f'Cliente {self.id} de reservaciones reserva un lugar')
                    self.monitor.notify()
                    time.sleep(15)
                else:
                    print(f'Cliente {self.id} intento reservar pero no tuvo exito, ya no hay cupo, por lo tanto, se va a la cola de espera')
                    clientes_pause.put(self.id)
                    time.sleep(25)
                self.id = self.id + 1

    def run(self):
        self.reservar()

class Mesero(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.monitor = threading.Condition()

    def atender(self):
        while True:
            with self.monitor:
                if not capacidad.empty() and capacidad.qsize()>1:
                    if meseros.empty():
                        meseros.put(1)
                        print(f'Un mesero esta disponible y tomando la orden')
                        time.sleep(3)
                        print(f'La orden esta en proceso')
                        ordenes.put(1)
                        meseros.get()
                        self.monitor.notify()
                    else:
                        print(f'Los meseros no se encuentran disponibles')
                        time.sleep(3)
                else:
                    print(f'Los meseros estan descansando')
                    time.sleep(3)

    def run(self):
        self.atender()

class Cocinero(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.monitor = threading.Condition()

    def cocinar(self):
        while True:
            with self.monitor:
                if not ordenes.empty():
                    if cocineros.empty():
                        cocineros.put(1)
                        print(f'Un cocinero esta cocinando')
                        time.sleep(4)
                        ordenes.get()
                        print(f'La orden esta lista')
                        cocineros.get()
                        ordenes_finalizadas.put(1)
                        self.monitor.notify()
                    else:
                        print(f'Los cocineros estan ocupados')
                        time.sleep(4)

    def run(self):
        self.cocinar()

class Recepcionista(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.monitor = threading.Condition()
        self.id = id

    def atender(self):
        while True:
            with self.monitor:
                if reservaciones.qsize() > 2:
                    capacidad.put(self.id)
                    print(f'Cliente {self.id} con una reservacion fue atendido')
                    reservaciones.get()
                    self.monitor.notify()
                    time.sleep(5)
                else:
                    if clientes_pause.empty():
                        if not capacidad.full():
                            capacidad.put(self.id)
                            print(f'Cliente {self.id} fue atendido exitosamente')
                            self.monitor.notify()
                            time.sleep(4)
                        else:
                            print(f'Cliente {self.id} esta en cola de espera')
                            clientes_pause.put(self.id)
                            print(f'Hay {clientes_pause.qsize()} clientes en cola de espera')
                            time.sleep(8)
                    else:
                        print(f'Cliente {self.id} esta en cola de espera')
                        clientes_pause.put(self.id)
                        print(f'Hay {clientes_pause.qsize()} clientes en cola de espera')
                        time.sleep(5)
            self.id = self.id + 1

    def run(self):
        self.atender()

if __name__ == '__main__':
    hilo_recepcion = Recepcionista(1)
    hilo_recepcion.start()
    hilo_cliente = Cliente(1)
    hilo_cliente.start()
    hilo_reservacion = Reservacion(1)
    hilo_reservacion.start()
    hilo_mesero = Mesero()
    hilo_mesero.start()
    hilo_cocinero = Cocinero()
    hilo_cocinero.start()
