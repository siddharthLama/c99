import time
import os
import shutil

path = input("Path of the folder or file :-")
days=0
seconds=time.time()-(days*24*60*60)

if (os.path.exists(path)):
    for root,dirs,files in os.walk(path,topdown=True):
        for name in files:
            path=os.path.join(root,name)
            ctime=os.stat(path).st_ctime

            if(seconds>=ctime):
                os.remove(path)
                print("\n Deleted this path"+ path +"sucessfully")

        for name in dirs:
            path = os.path.join(root, name)
            ctime = os.stat(path).st_ctime

            if (seconds >= ctime):
                shutil.rmtree(path)
                print("\n Deleted the path " + path + " successfully")
else:
    print("\n File/Folder not found")