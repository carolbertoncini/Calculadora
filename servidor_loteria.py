import socket
import random

PORT = 9087
IP = "10.108.33.34"
MAX_OPEN_REQUESTS = 5

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    def process_client(clientesocket): 
        servidor.bind((IP, PORT))
        servidor.listen(MAX_OPEN_REQUESTS)
        print('Esperando conexion en {IP},{PORT}'.format(IP = IP, PORT = PORT))
        numero = random.randint(0, 9)
        (cliente, direccion) = servidor.accept()
        #Voy a coger el IP del cliente 
        IP = clientesocket.getpeername()
        IP = IP.split(".")
        suma = 0
        for i in IP:
            i = int(i)
            suma += i
        resto = suma % 10
        if resto == numero:
            print("TE HA TOCADO. EL NUMERO ERA: ", resto)
        else:
            print("NO TE HA TOCADO. TU NUMERO ERA: ", resto)
        clientesocket.close()
 
    process_client(clientesocket)



except socket.error:
    print("Ha habido un problema en el servidor")
    cliente.close()
    servidor.close()
