import sys, re, copy 

def partOne(inpu) :
    with open(inpu,'r') as inp:
        coord=[["E",0],["S",0],["W",0],["N",0]]
        fac=0
        for i in inp :
            ins=i[:-1]
            order=ins[0]
            value=int(ins[1:])
            if order == "R" :
                fac=(fac+int(value/90))%4
            elif order == "L" :
                fac=(fac-int(value/90))%4
            elif order == "F" :
                coord[fac][1]+=value
            else :
                if order == "E" :
                    ind=0
                elif order == "S" :
                    ind=1
                elif order == "W" :
                    ind=2
                elif order == "N" :
                    ind=3
                coord[ind][1]+=value
        return abs(coord[0][1]-coord[2][1])+abs(coord[1][1]-coord[3][1])



print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp:
        coord=[["E",10],["S",0],["W",0],["N",1]]
        pos=[["E",0],["S",0],["W",0],["N",0]]
        p=0
        for i in inp :
            p+=1
            ins=i[:-1]
            order=ins[0]
            value=int(ins[1:])
            if order == "R" :
                shift=int(value/90)%4
                c=0
                newCoord=[]
                while c<len(coord) :
                    newCoord.append([coord[c][0],coord[(c-shift)%4][1]])
                    c+=1
                coord=copy.deepcopy(newCoord)
            elif order == "L" :
                shift=int(value/90)%4
                c=0
                newCoord=[]
                while c<len(coord) :
                    newCoord.append([coord[c][0],coord[(c+shift)%4][1]])
                    c+=1
                coord=copy.deepcopy(newCoord)
            elif order == "F" :
                c=0
                while c<len(pos) :
                    pos[c]=[pos[c][0],pos[c][1]+(coord[c][1]*value)]
                    c+=1
            else :
                if order == "E" :
                    ind=0
                elif order == "S" :
                    ind=1
                elif order == "W" :
                    ind=2
                elif order == "N" :
                    ind=3
                coord[ind][1]+=value
        return abs(pos[0][1]-pos[2][1])+abs(pos[1][1]-pos[3][1])

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
