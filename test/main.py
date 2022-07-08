import os
import re
import telebot


myf = open('test\.env','r')
print(myf)


arrFile = []
for i in myf.readlines():
    arrFile.append(i)

print(arrFile[0])