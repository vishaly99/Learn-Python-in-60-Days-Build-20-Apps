#Coding Exercise 1
from random import randrange

from numpy.random import random

lowerbond=int(input("Enter the lower bond:="))
upperbond=int(input("Enter the upper bond:="))

result=randrange(lowerbond,upperbond)
print(result)