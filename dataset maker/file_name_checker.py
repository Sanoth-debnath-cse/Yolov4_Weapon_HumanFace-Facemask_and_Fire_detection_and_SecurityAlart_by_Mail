import os
arr = os.listdir()
garbage_name=[]
print(len(arr))
for i in arr:
    x=i.split('.')
    #print(len(x))
    if len(x)>2:
        garbage_name.append(i)
print(len(garbage_name))
print(garbage_name)
'''for x in garbage_name:
    os.remove(x)'''
#print(pp)