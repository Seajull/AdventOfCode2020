import sys, re, copy 

def partOne(inpu) :
    with open(inpu,'r') as inp:
        c=0
        for i in inp :
            if c==0 :
                minDepart=int(i[:-1])
                c+=1
            else :
                bus=i[:-1]
        bus=bus.split(",")
        listBusTime=[]
        for j in bus :
            if j!="x" :
                tim=0
                while tim<minDepart:
                    tim+=int(j)
                listBusTime.append((j,tim))
        minTime=0
        idB=0
        for i in listBusTime :
            if minTime==0 :
                minTime=i[1]
                ids=i[0]
            elif i[1]<minTime :
                minTime=i[1]
                ids=i[0]
        return (minTime-minDepart)*int(ids)


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()
from sympy.ntheory.modular import crt
def partTwo(inpu) :
    with open(inpu,'r') as inp:
        c=0
        for i in inp :
            if c==0 :
                c+=1
                continue
            else :
                bus=i[:-1]
        bus=bus.split(",")
        busClean=[]
        c=0
        for i in bus :
            if i!="x" :
                if c==0 :
                    busClean.append((int(i),c))
                else :
                    busClean.append((int(i),int(i)-c))
            c+=1
        busID=[x[0] for x in busClean]
        busREM=[x[1] for x in busClean]
        return(crt(busID,busREM)[0])



print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()
