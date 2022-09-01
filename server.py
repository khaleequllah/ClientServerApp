import socket
import threading


HEADER = 64
Format = 'UTF-8'
Port = 5050
# For getting an Loopback Ip Address
# Hostname = socket.gethostname()
# Server = socket.gethostbyname(Hostname)
# Server2 = socket.gethostbyname_ex(socket.gethostname())

# For getting a router assigned IP Address


def getNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 0))
    return s.getsockname()[0]


# IP Address
Server = getNetworkIp()

DISCONNECT_MESSAGE = "!DISCONNECTED"


# ADDRESS
ADDR = (Server, Port)

# socket for server using TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[New Connection] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(Format)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(Format)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            # printing msg and address from where i came.
            print(f"[{addr}] {msg}")

    conn.close()


def start():
    server.listen()
    print(f"[Listening] Server is listening on {Server}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active Connections] {threading.active_count() -1}")


print("[Starting] server is starting......")
start()
