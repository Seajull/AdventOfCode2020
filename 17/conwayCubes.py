import sys, re, copy 

def partOne(inpu) :
    with open(inpu,'r') as inp:
        mapd={}
        z=0
        y=0
        for i in inp :
            x=0
            for j in i[:-1] :
                mapd[(z,y,x)]=j
                x+=1
            y+=1
#        newmapd=copy.deepcopy(mapd)
#        for coord in mapd :
#            for voisin in getVoisin(coord) :
#                if voisin not in newmapd.keys() :
#                    newmapd[voisin]="."
#        mapd=copy.deepcopy(newmapd)
        cycle=6
        c=0
        while c<cycle :
            newmapd=copy.deepcopy(mapd)
            for coord in mapd :
                for voisin in getVoisin(coord) :
                    if voisin not in newmapd.keys() :
                        newmapd[voisin]="."
            mapd=copy.deepcopy(newmapd)
            for i in mapd:
                voisin=getVoisin(i)
                validVois=[]
                for v in voisin :
                    if v in mapd.keys():
                        validVois.append(mapd[v])
                    else :
                        validVois.append(".")
                validCount=(validVois.count("#"))
                if mapd[i]=="." :
                    if validCount==3 :
                        newmapd[i]="#"
                    else :
                        newmapd[i]="."
                else :
                    if validCount==3 or validCount==2 :
                        newmapd[i]="#"
                    else :
                        newmapd[i]="."
            mapd=copy.deepcopy(newmapd)
            c+=1
        return list(mapd.values()).count("#")

def getVoisin(coord) :
    voisin=[]
    z=coord[0]
    y=coord[1]
    x=coord[2]
    tz=z-1
    while tz<=z+1 :
        ty=y-1
        while ty<=y+1 :
            tx=x-1
            while tx<=x+1 :
                voisin.append((tz,ty,tx))
                tx+=1
            ty+=1
        tz+=1
    voisin.remove(coord)
    return(voisin)

    



print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp:
        mapd={}
        z=0
        y=0
        w=0
        for i in inp :
            x=0
            for j in i[:-1] :
                mapd[(w,z,y,x)]=j
                x+=1
            y+=1
        cycle=6
        c=0
        while c<cycle :
            newmapd=copy.deepcopy(mapd)
            for coord in mapd :
                for voisin in getVoisin2(coord) :
                    if voisin not in newmapd.keys() :
                        newmapd[voisin]="."
            mapd=copy.deepcopy(newmapd)
            for i in mapd:
                voisin=getVoisin2(i)
                validVois=[]
                for v in voisin :
                    if v in mapd.keys():
                        validVois.append(mapd[v])
                    else :
                        validVois.append(".")
                validCount=(validVois.count("#"))
                if mapd[i]=="." :
                    if validCount==3 :
                        newmapd[i]="#"
                    else :
                        newmapd[i]="."
                else :
                    if validCount==3 or validCount==2 :
                        newmapd[i]="#"
                    else :
                        newmapd[i]="."
            mapd=copy.deepcopy(newmapd)
            c+=1
        return list(mapd.values()).count("#")

def getVoisin2(coord) :
    voisin=[]
    w=coord[0]
    z=coord[1]
    y=coord[2]
    x=coord[3]
    tw=w-1
    while tw<=w+1:
        tz=z-1
        while tz<=z+1 :
            ty=y-1
            while ty<=y+1 :
                tx=x-1
                while tx<=x+1 :
                    voisin.append((tw,tz,ty,tx))
                    tx+=1
                ty+=1
            tz+=1
        tw+=1
    voisin.remove(coord)
    return(voisin)

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()
