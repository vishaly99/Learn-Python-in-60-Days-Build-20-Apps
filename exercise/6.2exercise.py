filesname=['doc.txt','report.txt','presentation.txt']
msg="Hello"

for i in filesname:
    file=open("../file/"+i,'w')
    file.writelines(msg)
    print(i)
    file.close()