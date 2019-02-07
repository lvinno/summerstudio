# -*- coding: UTF-8 -*-
import os
import os.path
import glob


route = 'data/Siamese1'
path = os.getcwd()+'/'+route+'/'
files= os.listdir(path) #

n=0
for file in files: #遍历文件夹
     #设置旧文件名（就是路径+文件名）
     oldname=path+file
     #设置新文件名
     newname=path+'a'+str(n+1)+'.JPG'
     #用os模块中的rename方法对文件改名
     os.rename(oldname,newname)
     print(oldname,'======>',newname)
     n+=1