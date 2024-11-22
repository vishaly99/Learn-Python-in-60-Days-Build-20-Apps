import glob

from numpy.core.defchararray import upper

myfiles=glob.glob("file/*.txt")

for filepath in myfiles:
    with open(filepath,'r') as file:
        print(file.read().upper())