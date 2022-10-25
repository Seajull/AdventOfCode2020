import sys

def partOne(inpu) :
    with open(inpu,'r') as inp :
        maxid=0
        for i in inp :
            bp=i[:-1]
            ran=(0,127)
            sid=getID(bp,ran)
            if sid > maxid :
                maxid=sid
    return maxid

def getID(bp,ran,row=0) :
    if bp :
        if len(bp)==3 :
            ran=(0,7)
        elif len(bp)==4 :
            if bp[0]=="F":
                row=ran[0]
            else :
                row=ran[1]
        elif len(bp)==1 : 
            if bp[0]=="L" :
                col=ran[0]
            else :
                col=ran[1]
            return((row*8)+col)

        if bp[0]=="F" :
            ran=(ran[0],(round(ran[1]/2)-1)+(round(ran[0]/2)))
        elif bp[0]=="B" :
            ran=(round(ran[1]/2)+round(ran[0]/2),ran[1])
        elif bp[0]=="L":
            ran=(ran[0],(round(ran[1]/2)-1)+(round(ran[0]/2)))
        elif bp[0]=="R":
            ran=(round(ran[1]/2)+round(ran[0]/2),ran[1])
            pass
        bp=bp[1:]
        return getID(bp,ran,row)
    



print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

import re, itertools
def partTwo(inpu) :
    with open(inpu,'r') as inp :
        maxid=0
        listSid=[]
        lrow=list(range(0,128))
        lcol=list(range(0,8))
        seat=list(itertools.product(lrow,lcol))
        seat=[((x[0]*8)+x[1]) for x in seat]
        for i in inp :
            bp=i[:-1]
            ran=(0,127)
            listSid.append(getID2(bp,ran))
        unoc=list(set(listSid)^set(seat))
        c=0
        for i in unoc :
            if i==c :
                c+=1
            else :
                return(i)


def getID2(bp,ran,row=0) :
    if bp :
        if len(bp)==3 :
            ran=(0,7)
        elif len(bp)==4 :
            if bp[0]=="F":
                row=ran[0]
            else :
                row=ran[1]
        elif len(bp)==1 : 
            if bp[0]=="L" :
                col=ran[0]
            else :
                col=ran[1]
            return((row*8)+col)

        if bp[0]=="F" :
            ran=(ran[0],(round(ran[1]/2)-1)+(round(ran[0]/2)))
        elif bp[0]=="B" :
            ran=(round(ran[1]/2)+round(ran[0]/2),ran[1])
        elif bp[0]=="L":
            ran=(ran[0],(round(ran[1]/2)-1)+(round(ran[0]/2)))
        elif bp[0]=="R":
            ran=(round(ran[1]/2)+round(ran[0]/2),ran[1])
            pass
        bp=bp[1:]
        return getID2(bp,ran,row)

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


