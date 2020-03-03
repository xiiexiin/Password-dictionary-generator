# -*- coding: utf-8 -*-
import zipfile
import os
import platform
import uuid
import socket
import sys
import platform



def zip_to(zippath,filename,fs):  #压缩文件到制定目录,zip文件名
        zips = zipfile.ZipFile(zippath,'a')
        zips.write(fs,filename,zipfile.ZIP_DEFLATED)
        zips.close


def get_jpg(rootdir):
        fs = []
        fs_name = []
        for root, dirs, files in os.walk(rootdir,topdown = True):
                for name in files: 
                        _, ending = os.path.splitext(name)
                        if ending == ".jpg":
                                fs.append(os.path.join(root,name)) 
                                fs_name.append(os.path.join(name))   
        print (fs)
        for i in range(len(fs)):
                zip_to(ZIP_PATH + 'get_jpg.zip',fs_name[i],fs[i])


def get_txt(rootdir):    
        fs = []
        fs_name = []    
        for root, dirs, files in os.walk(rootdir,topdown = True):
                for name in files: 
                        _, ending = os.path.splitext(name)
                        if ending == ".txt":
                                fs.append(os.path.join(root,name))
                                fs_name.append(os.path.join(name))    
        print (fs)
        for i in range(len(fs)):
                zip_to(ZIP_PATH + 'get_txt.zip',fs_name[i],fs[i])


def get_doc(rootdir):
        fs = []
        fs_name = []    
        for root, dirs, files in os.walk(rootdir,topdown = True):
                for name in files: 
                        _, ending = os.path.splitext(name)
                        if ending == ".doc":
                                fs.append(os.path.join(root,name))   
                                fs_name.append(os.path.join(name)) 
        print (fs)
        for i in range(len(fs)):
                zip_to(ZIP_PATH + 'get_doc.zip',fs_name[i],fs[i])


def get_mp4(rootdir):    
        fs = []  
        fs_name = []  
        for root, dirs, files in os.walk(rootdir,topdown = True):
                for name in files: 
                        _, ending = os.path.splitext(name)
                        if ending == ".mp4":
                                fs.append(os.path.join(root,name))  
                                fs_name.append(os.path.join(name))  
        print (fs)
        for i in range(len(fs)):
                zip_to(ZIP_PATH + 'get_mp4.zip',fs_name[i],fs[i])


def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])


def main():
  get_jpg(GET_PATH)
  get_txt(GET_PATH)
  get_doc(GET_PATH)
  get_mp4(GET_PATH)

if __name__ == '__main__' :
        myname = socket.getfqdn(socket.gethostname())  # 获取本机电脑名
        myaddr = socket.gethostbyname(myname)  # 获取本机ip
        os_name = ("OS: " + platform.platform())
        mache_name = ("主机名：" + myname)
        IP_addr = ("IP: " + myaddr)
        MAC_addr = ("MAC: " + get_mac_address())
        # if ((os_name[4:7]) == 'Win'):
        #         GET_PATH = 'C:/Program Files (x86)'
        #         ZIP_PATH = 'C:/Program Files (x86)/'
        # elif (os_name[4:7] == 'Lin'):
        #         GET_PATH = '/sys'
        #         ZIP_PATH = '/sys/'
        # else:
        #         exit(0)
        print (os_name)
        print(mache_name)
        print(IP_addr)
        print(MAC_addr)
        GET_PATH = '/home/lwc/files'  # 从该文件夹搜集文件
        ZIP_PATH = '/home/lwc/files/'  # 压缩到这个文件夹下面
        main()

