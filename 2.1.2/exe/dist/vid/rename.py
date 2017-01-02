from glob import glob
from os import rename

crk=list('BC2DFGHJKLMNPRS1TVZW')
sam=list('AXEIOQU')
name=0
c_sam=0
c_crk=0
for i in range (146):
    name=name+1
    if c_sam>6:
        c_sam=0
        c_crk=c_crk+1
    rename(str(name)+'.wav', crk[c_crk]+sam[c_sam]+'.wav')
    c_sam=c_sam+1
