
#!usr/bin/python
# -*- coding: utf-8 -*-
import zipfile
import rarfile

zfile = rarfile.RarFile("***********password.rar")

def delblankline(infile, outfile):
 infopen = open(infile, 'r',encoding="utf-8")
 outfopen = open(outfile, 'w',encoding="utf-8")
 db = infopen.read()
 outfopen.write(db.replace(' ','\n'))
 infopen.close()
 outfopen.close()
 
delblankline('************password.txt', "**********/new_password.txt")
passFile = open('**********/new_password.txt')

for line in passFile.readlines():
    pwd1 = line.strip('\n')
    try:
        zfile.extractall(path='********rar_file******', members=zfile.namelist(), pwd=pwd1)
        print(pwd1)
    except:
        pass
