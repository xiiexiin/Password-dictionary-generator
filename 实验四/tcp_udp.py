# -*- coding: utf-8 -*-
import os,subprocess
import platform

def shell(cmd):   #在终端执行指令，然后输出
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.readlines()
    for line in out:
        print (line.strip())


if __name__ == '__main__' :
    os_name = ("OS: " + platform.platform())
    if ((os_name[4:7]) == 'Lin'):
        print ("TCP OPEN PORT:")
        shell("netstat -ntpl")
        print ("UDP OPEN PORT:")
        shell("netstat -nupl")
    if ((os_name[4:7]) == 'Win'):
        print ("OPEN PORT:")
        shell("netstat -na")
    
