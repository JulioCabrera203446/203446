# Gerson Efher Lopez
# Julio Antonio Cabrera Yañez

import threading, random
import time
from queue import Queue

mutex = threading.Lock()

MESEROS = 2
COCINEROS = 2
clientes = Queue(maxsize=20)
cola_clientes = Queue()
reservaciones = Queue(maxsize=4) 
ordenes = Queue()
ordenes_listas = Queue()


class Reservacion(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.monitor = threading.Condition()

    def reservar(self):
        while True:
            with self.monitor:
                if reservaciones.full() == False:
                    reservaciones.put(self.id)
                    print("Cliente " +str(self.id)+ " ha reservado un lugar")
                    time.sleep(40)
                    self.id += 1
                else:
                    print("Cliente " +str(self.id)+ " no pudo reservar, se mando a la cola de clientes")
                    cola_clientes.put(self.id)
                    time.sleep(40)
                    self.id += 1

    def run(self):
        self.reservar()


class Atender(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.monitor = threading.Condition()

    def atender_cliente(self):
        while True:
            with self.monitor:
                if cola_clientes.empty():
                    if reservaciones.empty() == False:
                        reservaciones.get()
                        print("Cliente " +str(self.id)+ " con reservacion se atendio")
                        clientes.put(self.id)
                        time.sleep(3)
                    else:
                        if clientes.full() == False:
                            clientes.put(self.id)
                            print("Cliente " +str(self.id)+ " ha sido atendido")
                            time.sleep(3)
                        else:
                            print("Cliente " +str(self.id)+ " no pudo ser atendido, se mando a la cola de espera")
                            cola_clientes.put(self.id)
                            time.sleep(4)
                self.id += 1

    def run(self):
        self.atender_cliente()


class Cliente(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.monitor = threading.Condition()

    def comer(self):
        while True:
            with self.monitor:
                if ordenes_listas.empty() == False:
                    client_id = clientes.get()
                    print("Cliente " +str(client_id)+ " esta comiendo...")
                    ordenes_listas.get()
                    time.sleep(2)
                    print("Cliente " +str(client_id)+ " termino de comer y se fue del restaurante")
                    time.sleep(4)
            time.sleep(1)

    def run(self):
        self.comer()


class Cocinero(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.monitor = threading.Condition()

    def cocinar(self):
        while True:
            with mutex:
                if ordenes.empty() == False:
                    print("Cocinero esta cocinando...")
                    ordenes.get()
                    time.sleep(2)
                    print("Cocinero termino de cocinar una orden")
                    ordenes_listas.put(1)
                    time.sleep(3)
                else:
                    print("Cocinero esta esperando ordenes...")
                    time.sleep(3)

    def run(self):
        self.cocinar()


class Mesero(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.monitor = threading.Condition()

    def servir(self):
        while True:
            with mutex:
                if clientes.empty() == False:

                    print("Mesero esta atendiendo...")
                    time.sleep(2)
                    print("Mesero termino de atender a un cliente y genero una orden")
                    ordenes.put(1)
                    time.sleep(2)
                else:
                    print("Mesero esta esperando clientes...")
                    time.sleep(2)

    def run(self):
        self.servir()


if __name__ == "__main__":

    atender = Atender(1)
    atender.start()

    cliente = Cliente()
    cliente.start()

    reservacion = Reservacion(1)
    reservacion.start()

    for i in range(MESEROS):
        mesero = Mesero()
        mesero.start()

    for i in range(COCINEROS):
        cocinero = Cocinero()
        cocinero.start()
