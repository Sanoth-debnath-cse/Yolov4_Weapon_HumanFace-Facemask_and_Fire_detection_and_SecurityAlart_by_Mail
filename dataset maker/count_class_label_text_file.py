import glob
print(len(glob.glob('*.jpg')))
print(len(glob.glob('*.txt')))
count_mask=0
count_notmask=0
count_other=0
c_new=0
for item in glob.glob('*.txt'):
    ff=open(item,'r+').readlines()
    new_ff=[]
    for line in ff:
        x=line.split()
        #x[0]='2'
        if x[0]=='0':
            count_notmask+=1
        elif x[0]=='1':
            count_mask+=1
        elif x[0]=='2':
            count_other+=1
        else:
            c_new+=1
        #new_ff.append(x)
        #print(new_ff)
        #print(len(new_ff))
#print(new_ff)
print("smoke class",count_mask)
print('Fire class',count_notmask)
print('unknown class',count_other)
print('other',c_new)
