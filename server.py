import socket
from threading import Thread

host = 'localhost'
port = 8080
clients = {}
addresses = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

def broadcast(msg, prefix=""):
    for x in clients:
        x.send(bytes(prefix, "utf8") + msg)

def handle_clients(conn, address):
    name = conn.recv(1024).decode()
    welcome = "Welcome " + name + ". You can type #quit if you ever want to leave the Chat Room"
    conn.send(bytes(welcome, "utf8"))
    msg = name + " has recently joined the chat room"
    broadcast(bytes(msg, "utf8"))
    clients[conn] = name

    while True:
        msg = conn.recv(1024).decode()
        if msg != bytes("#quit", "utf8"):
            #broadcast(bytes(name + ": " + msg, "utf8"))
            broadcast(msg, name +": ")
        else:
            conn.send(bytes("#quit", "utf8"))
            conn.close()
            del clients[conn]
            broadcast(bytes(name + " has left the chat room.", "utf8"))

def accept_client_connections():
    while True:
        conn, address = sock.accept()
        print(address, " Has Connected!")
        message = "Welcome to the Chat Room, Please Type your name to continue"
        conn.send(message.encode('utf8'))
        addresses[conn] = address 

        Thread(target = handle_clients, args = (conn, address)).start()

if __name__ == "__main__":
    sock.listen(5)    
    print("The server is running and listening to clients requests")

    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join()




conn.close()