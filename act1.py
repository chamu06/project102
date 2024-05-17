import os
import shutil
source="C:/Users/charm/Downloads"
destination="C:/Users/charm/Downloads/C102"
listoffiles=os.listdir(source)
#print(listoffiles)
for file in listoffiles:
    name,extension=os.path.splitext(file)
    #print(name)
    #print(extension)
    if extension=="":
        continue
    if extension in [".pdf",".txt",".docx",".xlsx"]:
        path1=source+"/"+file
        path2=destination+"/"+"docfile"
        path3=destination+"/"+"docfile"+"/"+file
        print(path1)
        print(path3)

        if os.path.exists(path2):
            print("file is moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("file is moving")
            shutil.move(path1,path3)