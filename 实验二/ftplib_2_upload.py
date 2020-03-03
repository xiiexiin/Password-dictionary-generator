from ftplib import FTP
#连接并登录
def ftpconnect(host,port,username, password):
    ftp = FTP()
    ftp.connect(host, port)          #连接
    ftp.login(username, password)  #登录，如果匿名登录则用空串代替即可
    return ftp


#下载文件
def downloadfile(ftp, remotepath, localpath):  #remotepath：上传服务器路径；localpath：本地路径；
    bufsize = 1024                #设置缓冲块大小
    fp = open(localpath,'wb')     #以写模式在本地打开文件
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize) #接收服务器上文件并写入本地文件
    fp.close()


#上传文件
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR '+ remotepath , fp, bufsize)    #上传文件
    fp.close()

if __name__ == "__main__":
    ftp = ftpconnect("192.168.64.1",21, "xiiexiin", "123456") #IP,port,username,userpassword
    uploadfile(ftp, "/get_doc.zip", "D:/课程学习/大四下/网络攻防实践/yh实验/实验二/test/get_doc.zip")#上传后的文件名,客户端文件名
    uploadfile(ftp, "/get_mp4.zip", "D:/课程学习/大四下/网络攻防实践/yh实验/实验二/test/get_mp4.zip")
    uploadfile(ftp, "/get_txt.zip", "D:/课程学习/大四下/网络攻防实践/yh实验/实验二/test/get_txt.zip")
    uploadfile(ftp, "/get_jpg.zip", "D:/课程学习/大四下/网络攻防实践/yh实验/实验二/test/get_jpg.zip")
    ftp.quit()
