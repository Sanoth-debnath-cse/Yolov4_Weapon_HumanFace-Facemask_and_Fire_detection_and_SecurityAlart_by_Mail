import os
path=os.chdir('')
i=0
for file in os.listdir(path):
    new_file_name="FireDataV9_1_{}.txt".format(i)
    os.rename(file, new_file_name)
    i+=1