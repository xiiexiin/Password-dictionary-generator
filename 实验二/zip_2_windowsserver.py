from ftplib import FTP

def ftpconnect(host,port,username, password):#连接并登录
    ftp = FTP()
    ftp.connect(host, port)                   #连接
    ftp.login(username, password)             #登录，如果匿名登录则用空串代替即可
    return ftp


#下载文件
def downloadfile(ftp, remotepath, localpath):             #remotepath：上传服务器路径；localpath：本地路径；
    bufsize = 1024                                          #设置缓冲块大小
    fp = open(localpath,'wb')                               #以写模式在本地打开文件
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
    uploadfile(ftp, "/get_doc.zip", "******************压缩文件路径***********/get_doc.zip")#上传后的文件名,客户端文件名
    uploadfile(ftp, "/get_mp4.zip", "******************压缩文件路径***********/get_mp4.zip")
    uploadfile(ftp, "/get_txt.zip", "******************压缩文件路径***********/get_txt.zip")
    uploadfile(ftp, "/get_jpg.zip", "******************压缩文件路径***********/get_jpg.zip")
    ftp.quit()
