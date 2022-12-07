import socket
from States import State as STATE
from Constants import Constants as const
import threading


#client side
def createClient():
    STATE.ADDRESS = (STATE.SERVER_ID, const.PORT)
    STATE.SOCKET_CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print(f"[CONNECTION PENDING] Attempting to connect to server {STATE.SERVER_ID}")
    STATE.SOCKET_CONNECTION.connect(STATE.ADDRESS)
    print(f"[CONNECTED]")
    conn, addr = STATE.SOCKET_CONNECTION.accept()
    STATE.CONNECTION_THREAD = threading.Thread(target=clientListen, args=(conn, addr))
    print("[STARTING GAME]")
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
            print(f"[MSG RECEIVED] {msg}")
            STATE.RECIEVED_MSG_QUEUE.put(msg)

            if(msg[0] == 'd'):
                connected = False
    conn.close()

#server side
def createServer():
    STATE.SERVER_ID = socket.gethostbyname(socket.gethostname())
    STATE.ADDRESS = (STATE.SERVER_ID, const.PORT)

    STATE.SOCKET_CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    STATE.SOCKET_CONNECTION.bind(STATE.ADDRESS)

    STATE.SOCKET_CONNECTION.listen()
    print(f"[SERVER CREATED] Your server address is: {STATE.SERVER_ID} . Provide this address to your oppponent.")
    print('[WAITING] Now waiting for opponent to connect')
    STATE.CLIENT_TUPLE = STATE.SOCKET_CONNECTION.accept()
    STATE.CONNECTION_THREAD = threading.Thread(target=handleClient, args=(STATE.CLIENT_TUPLE[0], STATE.CLIENT_TUPLE[1]))
    
    STATE.CLIENT_TUPLE[0].recv(const.HEADER_LENGTH).decode(const.FORMAT) #waits until connection pings connected msg
    print("[CONNECTED] Game will now start")

    STATE.CONNECTION_THREAD.start()
    print("[DISCONNECTED]")

def serverSend(msg):
    conn = STATE.CLIENT_TUPLE[0]
    message = msg.encode(const.FORMAT)
    msg_length = len(message)
    header = str(msg_length).encode()
    header += b' ' * (const.HEADER_LENGTH - len(header))
    conn.send(header)
    conn.send(message)


def handleClient(conn, addr):

    connected = True
    while connected:
        msgHeader = conn.recv(const.HEADER_LENGTH).decode(const.FORMAT)
        if(msgHeader):
            msgLength = int(msgHeader)
            msg = conn.recv(msgLength).decode(const.FORMAT)
            print(f"[MSG RECEIVED] {msg}")
            STATE.RECIEVED_MSG_QUEUE.put(msg)

            if(msg[0] == 'd'):
                connected = False
    conn.close()

#both sides
def sendMsg(msg):
    if(STATE.IS_HOST):
        serverSend(msg)
    else:
        clientSend(msg)


def getAddress():
    return socket.gethostbyname(socket.gethostname())