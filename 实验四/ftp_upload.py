from ftplib import FTP
#连接并登录
def ftpconnect(host,port,username, password):
    ftp = FTP()
    #ftp.set_debuglevel(2)         #打开调试级别2，显示详细信息
    ftp.connect(host, port)          #连接
    ftp.login(username, password)  #登录，如果匿名登录则用空串代替即可
    return ftp
#下载文件
def downloadfile(ftp, remotepath, localpath):  #remotepath：上传服务器路径；localpath：本地路径；
    bufsize = 1024                #设置缓冲块大小
    fp = open(localpath,'wb')     #以写模式在本地打开文件
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize) #接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)         #关闭调试
    fp.close()                    #关闭文件
#上传文件
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR '+ remotepath , fp, bufsize)    #上传文件
    ftp.set_debuglevel(0)
    fp.close()

if __name__ == "__main__":
    ftp = ftpconnect("192.168.*.*",21, "yourname", "password")   #ftp服务端ip，用户名和密码
    #downloadfile(ftp, "***", "***")
    uploadfile(ftp, "hello.txt", "/home/....../hello.txt")   
    uploadfile(ftp, "get_doc.zip", "/home/....../get_doc.zip")   
    uploadfile(ftp, "get_jpg.zip", "/home/....../get_jpg.zip")
    uploadfile(ftp, "get_mp4.zip", "/home/....../get_mp4.zip")
    uploadfile(ftp, "get_txt.zip", "/home/....../get_txt.zip")
    ftp.quit()
