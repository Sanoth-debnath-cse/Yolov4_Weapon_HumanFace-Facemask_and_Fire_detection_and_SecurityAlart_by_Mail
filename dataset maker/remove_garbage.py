import os
arr = os.listdir()
pp=[]
print(len(arr))
for i in arr:
    x=i.split('.')
    #print(len(x))
    pp.append(x[0])
#print(pp)
d={}
for j in pp:
    d[j]=d.get(j,0)+1
#print(d)
ls=[]
for k in d:
    if d[k]!=2:
        ls.append(k)

print(len(ls))
#print(ls)

deleted_ls=[]
for a in ls:
    for b in arr:
        if a==b.split('.')[0]:
            #print(b)
            deleted_ls.append(b)
print(deleted_ls)
print(len(deleted_ls))
for x in deleted_ls:
    os.remove(x)