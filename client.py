from re import M
import socket


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
ADDR = (Server, Port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(Format)
    msg_length = len(message)
    send_length = str(msg_length).encode(Format)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("Hello World!")
