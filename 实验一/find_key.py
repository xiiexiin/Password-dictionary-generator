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

# delblankline("***************/password11.txt")
# delblankline("***************/password21.txt")
# delblankline("***************/password31.txt")
# delblankline("***************/password41.txt")


def main():
 print("please input group_num:\n")
 g = int(input())
 print("please input pass_num:\n")
 num = int(input())

 keyfile = open("***************/password"+str(num)+"1.txt")

 keystr = []
 kk = []

 for l in keyfile.readlines():
     k = l.strip('\n')
     keystr.append(k)

 for ii in range (keystr.count('')):
     keystr.remove('')

 key = linecache.getline("***************/test.txt", g).split()

 for i in range (10):
    kk.append(key[i])

 for ii in range (10):
    n = int(kk[ii])-1
    print (keystr[n])

if __name__ == '__main__':
    main()