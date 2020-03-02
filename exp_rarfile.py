
#!usr/bin/python
# -*- coding: utf-8 -*-
import zipfile
import rarfile

zfile = rarfile.RarFile("/home/kali/Desktop/password.rar") 

def delblankline(infile, outfile):
 infopen = open(infile, 'r',encoding="utf-8")
 outfopen = open(outfile, 'w',encoding="utf-8")
 db = infopen.read()
 outfopen.write(db.replace(' ','\n'))
 infopen.close()
 outfopen.close()
 
delblankline('/home/kali/Desktop/password.txt', "/home/kali/Desktop/password4.txt")
passFile = open('/home/kali/Desktop/password4.txt')

for line in passFile.readlines():
    pwd1 = line.strip('\n')
    try:
        zfile.extractall(path='/home/kali/Desktop/', members=zfile.namelist(), pwd=pwd1)
        print(pwd1)
    except:
        pass
