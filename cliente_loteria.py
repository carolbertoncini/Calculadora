import socket

IP = "10.108.33.34"
PORT = 9087

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#try:
cliente.connect((IP, PORT))
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("conexión establecida")

print(s.recv(2048).decode("utf-8"))
#except :
    #print("Ha habido un problema")
    #cliente.close()
