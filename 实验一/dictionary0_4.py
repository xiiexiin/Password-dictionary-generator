import itertools as its
words = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for k in range(1,5):
    r =its.product(words,repeat=k)
    dic = open("/home/...../dictionary.txt","a")
    for i in r:
        dic.write("".join(i))
        dic.write("".join("\n"))
    dic.close()
