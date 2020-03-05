# -*- coding: utf-8 -*-
import time
import socket
# import threading


def handle_data(sock, addr):
    print("Establishing a connection from %s:%s" % addr)
    sock.send(b'Start!')

    while True:
        # data = sock.recv(1024)
        # if not data:
        #     break
        # sock.send(data)
        # print(sock.recv(1024))

        command = input("Enter shell command or quit: ")
        sock.send(command.encode('utf-8'))
        if command == "quit": break
        data = sock.recv(1024)
        print(data.decode('gbk'))

    sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('192.168.*.*', 80))
    s.listen(5)
    while True:
        sock,addr = s.accept()
        print ("got a connection request")
        handle_data(sock,addr)
        # t = threading.Thread(target=handle_data, args=(sock, addr))
        # t.start()
