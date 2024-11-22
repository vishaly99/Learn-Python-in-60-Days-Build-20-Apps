filesname=['a.txt','b.txt','c.txt']

for i in filesname:
    file=open("../file/"+i,'r')
    msg=file.read()
    print(msg)
    file.close()