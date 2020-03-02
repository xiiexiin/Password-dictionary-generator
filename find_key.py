import string
import numpy as np
import linecache

def delblankline(infile, outfile):
 infopen = open(infile, 'r',encoding="utf-8")
 outfopen = open(outfile, 'w',encoding="utf-8")
 db = infopen.read()
 outfopen.write(db.replace(' ','\n'))
 infopen.close()
 outfopen.close()

# delblankline("D:/课程学习/大四下/网络攻防实践/yh实验/实验一/zip/password/password1.txt", "D:/课程学习/大四下/网络攻防实践/yh实验/实验一/zip/password/password11.txt")
# delblankline("D:/课程学习/大四下/网络攻防实践/yh实验/实验一/zip/password/password2.txt", "D:/课程学习/大四下/网络攻防实践/yh实验/实验一/zip/password/password21.txt")
# delblankline("D:/课程学习/大四下/网络攻防实践/yh实验/实验一/zip/password/password3.txt", "D:/课程学习/大四下/网络攻防实践/yh实验/实验一/zip/password/password31.txt")
# delblankline("D:/课程学习/大四下/网络攻防实践/yh实验/实验一/zip/password/password4.txt", "D:/课程学习/大四下/网络攻防实践/yh实验/实验一/zip/password/password41.txt")


def main():
 print("please input group_num:\n")
 g = int(input())
 print("please input pass_num:\n")
 num = int(input())

 keyfile = open("D:/课程学习/大四下/网络攻防实践/yh实验/实验一/zip/password/password"+str(num)+"1.txt")

 keystr = []
 kk = []

 for l in keyfile.readlines():
     k = l.strip('\n')
     keystr.append(k)

 for ii in range (keystr.count('')):
     keystr.remove('')

 key = linecache.getline("D:/课程学习/大四下/网络攻防实践/yh实验/实验一/test.txt", g).split()

 for i in range (10):
    kk.append(key[i])

 for ii in range (10):
    n = int(kk[ii])-1
    print (keystr[n])

if __name__ == '__main__':
    main()