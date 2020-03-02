#!usr/bin/python
# -*- coding: utf-8 -*-
import zipfile
zfile = zipfile.ZipFile("/home/lwc/Documents/学习/网络攻防/编程实验/第一天/zipfile/zip.zip") #要解压缩的压缩包
#passFile = open('/home/lwc/Documents/学习/网络攻防/编程实验/第一天/zipfile/password3.txt')
#error=1
#password="7j9STupy"
# -*- coding: utf-8 -*-
'''
遇到文中的空格就换行
'''
def delblankline(infile, outfile):
    infopen = open(infile, 'r',encoding="utf-8")
    outfopen = open(outfile, 'w',encoding="utf-8")
    db = infopen.read()
    outfopen.write(db.replace(' ','\n'))
    infopen.close()
    outfopen.close()
 
delblankline('/home/lwc/Documents/学习/网络攻防/编程实验/第一天/zipfile/password.txt', "/home/lwc/Documents/学习/网络攻防/编程实验/第一天/zipfile/password4.txt")
passFile = open('/home/lwc/Documents/学习/网络攻防/编程实验/第一天/zipfile/password4.txt')

for line in passFile.readlines():
    pwd1 = line.strip('\n')
    try:
        zfile.extractall(path='/home/lwc/Documents/学习/网络攻防/编程实验/第一天/zipfile/', members=zfile.namelist(), pwd=pwd1.encode('utf-8'))#进行解压缩操作，path为输出的路径
        print(pwd1)
    except:
        pass

