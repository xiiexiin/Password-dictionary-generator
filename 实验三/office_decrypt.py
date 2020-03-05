#多进程破解office
import time
import random
from multiprocessing import Process
import PyPDF4
import sys
import msoffcrypto


def OFFICE(off_path,pwd_path,out_path):
    print ("try")
    file = msoffcrypto.OfficeFile(open(off_path, "rb"))
    passFile = open(pwd_path)

    for line in passFile.readlines():
        pwd1 = line.strip('\n')
        #file.load_key(password = pwd1)

        try:
            file.load_key(password = pwd1)
            file.decrypt(open(out_path, "wb"))
            print(pwd1)
            break
        except:
            pass
    print ("进程结束")


if __name__ == '__main__':
    off_path = '/home/....../网络攻防实践.xlsx'
    pwd_path = ['/home/....../part_1.txt',
    '/home/....../part_2.txt',
    '/home/....../part_3.txt',
    '/home/....../part_4.txt',
    '/home/....../part_5.txt',
    '/home/....../part_6.txt',
    '/home/....../part_7.txt',
    '/home/....../part_8.txt']

    out_path = "/home/....../网络攻防实践破解.xlsx"

    p1=Process(target=OFFICE,args=(off_path,pwd_path[0],out_path,)) #必须加,号 
    p2=Process(target=OFFICE,args=(off_path,pwd_path[1],out_path,))
    p3=Process(target=OFFICE,args=(off_path,pwd_path[2],out_path,))
    p4=Process(target=OFFICE,args=(off_path,pwd_path[3],out_path,))
    p5=Process(target=OFFICE,args=(off_path,pwd_path[4],out_path,))
    p6=Process(target=OFFICE,args=(off_path,pwd_path[5],out_path,))
    p7=Process(target=OFFICE,args=(off_path,pwd_path[6],out_path,))
    p8=Process(target=OFFICE,args=(off_path,pwd_path[7],out_path,))
  

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    print('主线程')




