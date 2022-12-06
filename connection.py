import socket
from States import State as STATE
from Constants import Constants as const
import threading


#client side
def createClient():
    STATE.SOCKET_CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    STATE.SOCKET_CONNECTION.connect(STATE.ADDRESS)
    print(f"[CONNECTED] server = {STATE.ADDRESS}")
    conn, addr = STATE.SOCKET_CONNECTION.accept()
    STATE.CONNECTION_THREAD = threading.Thread(target=clientListen, args=(conn, addr))
    STATE.CONNECTION_THREAD.start()
    print("[DISCONNECTED]")
    


def clientSend(msg):
    message = msg.encode(const.FORMAT)
    msg_length = len(message)
    header = str(msg_length).encode()
    header += b' ' * (const.HEADER_LENGTH - len(header))
    STATE.SOCKET_CONNECTION.send(header)
    STATE.SOCKET_CONNECTION.send(message)

def clientListen(conn, addr):
    connected = True
    while connected:
        msgHeader = conn.recv(const.HEADER_LENGTH).decode(const.FORMAT)
        if(msgHeader):
            msgLength = int(msgHeader)
            msg = conn.recv(msgLength).decode(const.FORMAT)
            print(f"[{addr}] {msg}")

            if(msg == const.DISCONNECT_MSG):
                connected = False
    conn.close()

#server side
def createServer():
    STATE.SOCKET_CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    STATE.SOCKET_CONNECTION.bind(STATE.ADDRESS)

    STATE.SOCKET_CONNECTION.listen()
    print(f"[LISTENING] server is listening on {STATE.SERVER_ID}")
    conn, addr = STATE.SOCKET_CONNECTION.accept()
    STATE.CONNECTION_THREAD = threading.Thread(target=handleClient, args=(conn, addr))
    STATE.CONNECTION_THREAD.start()
    print("[DISCONNECTED]")

def handleClient(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msgHeader = conn.recv(const.HEADER_LENGTH).decode(const.FORMAT)
        if(msgHeader):
            msgLength = int(msgHeader)
            msg = conn.recv(msgLength).decode(const.FORMAT)
            print(f"[{addr}] {msg}")

            if(msg == const.DISCONNECT_MSG):
                connected = False
    conn.close()

