import socket
import threading

PORT = 5050
SERVER_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_NAME)
BUF_SIZE = 1024
ENCODING = "utf-8"


def receive_message(s):
    while True:
        msg_bytes = s.recv(BUF_SIZE)
        message = msg_bytes.decode(ENCODING)
        # TASK: do not print empty messages
        if s == "":
            pass
        print(f'Received: {message} ')

        # TASK:
        # send message to other clients, except current
        # CREATE A CLIENTS LIST
        clients = []
        # ADD CLIENTS TO LIST
        clients.append(SERVER_NAME)
        # ISOLATE MESSAGE SENDER
        msg_sender = socket.gethostname()
        # REMOVING MESSAGE SENDER FROM LIST
        clients.remove(msg_sender)
        # SENDING MESSAGE TO ALL CLIENTS IN A LIST
        for _ in clients:
            s.send(message)


# define an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reuse port:
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# set server to listen for incoming connections on given socket (SERVER_IP, PORT) tuple:
s.bind((SERVER_IP, PORT))
s.listen()

print(f"Server is listening on {SERVER_IP}:{PORT}. Name: {SERVER_NAME}")


while True:
    (conn, addr) = s.accept()
    print(conn, addr)

    # Each Client Connection should be handled in different thread
    tr = threading.Thread(target=receive_message, args=(conn,), daemon=True)
    # receive_message(conn)

    tr.start()


