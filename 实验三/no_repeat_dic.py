#生成秘钥长度为8位的各位不重复的字典
import itertools as its
words = "1234567890"         #秘钥空间
# for k in range(1,9):
#     r =its.product(words,repeat=k)
#     dic = open("/home/lwc/Documents/学习/网络攻防/编程实验/第一天/dictionary.txt","a")
#     for i in r:
#         dic.write("".join(i))
#         dic.write("".join("\n"))
#     dic.close()

#list1 = ['1','8'] #每一行中已经有的数字组成列表

#------  1800万-1900万

r =its.permutations(words,8)
#print (type(r))
dic = open("/home/....../big.txt","a") #生成的字典文件
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
    #list1.clear()    #清空列表
dic.close()