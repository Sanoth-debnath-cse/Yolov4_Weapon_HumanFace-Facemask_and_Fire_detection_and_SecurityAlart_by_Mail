#import os
import glob
print(len(glob.glob('*.txt')))
blank=[]
for item in glob.glob('*.txt'):
    ff=open(item,'r+').readlines()
    if len(ff)==0:
        blank.append(item)
print(len(blank))
print(blank)
'''for x in blank:
    os.remove(x)'''