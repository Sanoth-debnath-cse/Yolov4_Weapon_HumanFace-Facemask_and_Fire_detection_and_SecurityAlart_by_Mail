import glob
print(glob.glob('*.txt'))
for item in glob.glob('*.txt'):
    ff=open(item,'r+').readlines()
    new_ff=[]
    for line in ff:
        x=line.split()
        if x[0]=='0':
            x[0]='1'
            new_ff.append(x)
        #print(len(new_ff))
    with open(item,'w+') as ff:
        #for i in new_ff:
            #print(i)
        ff.writelines(' '.join(j for j in i)+'\n' for i in new_ff)