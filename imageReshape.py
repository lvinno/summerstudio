from PIL import Image
import os
import os.path
import glob

def convertjpg(jpgfile,outdir,width=250,height=250):
    img=Image.open(jpgfile).convert('RGB')
    try:
        new_img=img.resize((width,height),Image.BILINEAR)    
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)




route = 'data/n02123394'
path = os.getcwd()+'/'+route+'/' #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
print(files)
for file in files: #遍历文件夹
    print(path + file)
    convertjpg(path+file,os.getcwd()+'/'+route+"after/")