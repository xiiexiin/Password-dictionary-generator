import itertools as its
words = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for k in range(1,5):
    r =its.product(words,repeat=k)
    dic = open("/home/lwc/Documents/学习/网络攻防/编程实验/第一天/dictionary.txt","a")
    for i in r:
        dic.write("".join(i))
        dic.write("".join("\n"))
    dic.close()
