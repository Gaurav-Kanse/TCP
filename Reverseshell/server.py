import socket
import sys

def create_socket():
    try:
        global host 
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))

#Bind socket and listen for connections
def bind_socket():
    try:
        global host 
        global port
        global s
        print("Binding the Port: " + str(port))
        
        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()

#Establish connection with a client (socket must be listening)
def socket_accept():
    conn, addr = s.accept()
    print("Connection has been established | " + "IP " + addr[0] + " | Port " + str(addr[1]))
    send_commands(conn)
    conn.close()

#Send commands 
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()