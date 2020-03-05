import time
import random
from multiprocessing import Process
import PyPDF4
import sys

# def run(name):
#     print('%s runing' %name)
#     time.sleep(random.randrange(1,5))
#     print('%s running end' %name)

def PDF(pdfpath,pwdpath):
    pdfReader = PyPDF4.PdfFileReader(open(pdfpath,'rb'))
    if pdfReader.isEncrypted:
        print('try')
        File = open(pwdpath)
        sfile = File.read()
        dic = sfile.split('\n')
        num = len(dic)
        for i in range(num):
            #print('try '+str(i) +' ...')
            if pdfReader.decrypt(dic[i]):
                print(dic[i])
                #print('PDF有 '+ str(pdfReader.numPages) + '...')
                #print('内容摘要')
                pageObj = pdfReader.getPage(0)
                print(pageObj.extractText())
                break
            temp = dic[i].lower()
            if pdfReader.decrypt(temp):
                print(temp)
                #print('破解成功，密码是 ' + temp + '...')
                #print('PDF有 '+ str(pdfReader.numPages) + '...')
                #print('内容摘要')
                pageObj = pdfReader.getPage(0)
                print(pageObj.extractText())
                break
            #print('失败')
        print('程序关闭...')
        sys.exit()


if __name__ == '__main__':
    pdfpath = '/home/lwc/......../文档2.pdf'
    pwdpath = ['/home/lwc/....../part_1.txt',
                '......',
                '......']#根据文档分割和进程数增加

    p1=Process(target=PDF,args=(pdfpath,pwdpath[0],)) #必须加,号 
    p2=Process(target=PDF,args=(pdfpath,pwdpath[1],))
    '''
    ......   #有多少线程设多少个
    '''
    

    p1.start()
    p2.start()
    '''
    ...... #有多少线程设多少个
    '''
    #print('主线程')




