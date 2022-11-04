import sys, re, copy 

def partOne(inpu) :
    with open(inpu,'r') as inp:
        mat=[]
        for i in inp :
            mat.append(list(i[:-1]))
        maxy=len(mat[0])
        maxx=len(mat)

        newmat=copy.deepcopy(mat)
        c=0

#        for i in mat :
#            print("".join(i))
        while True:
            change=False
            x=0
            while x<maxx :
                y=0
                while y<maxy :
                    if mat[x][y]=="." :
                        y+=1
                        continue
                    elif mat[x][y]=="L" :
                        if nVoisin(mat,x,y)==0 :
                            newmat[x][y]="#"
                            change=True
                    elif mat[x][y]=="#" :
                        if nVoisin(mat,x,y)>=4 :
                            newmat[x][y]="L"
                            change=True
                    y+=1
                x+=1
            mat=copy.deepcopy(newmat)
#            for i in newmat :
#                print("".join(i))
            c+=1
            if not change :
                k=0
                for i in mat :
                    k+=i.count("#")
                return(k)

def nVoisin(mat,x,y) :
    maxy=len(mat[0])
    maxx=len(mat)
    voisin=[]
    voisin.append((x-1,y-1))
    voisin.append((x-1,y))
    voisin.append((x-1,y+1))
    voisin.append((x,y-1))
    voisin.append((x,y+1))
    voisin.append((x+1,y-1))
    voisin.append((x+1,y))
    voisin.append((x+1,y+1))
    validVoisin=[]
    for i in voisin :
        if not(-1 in i or i[1]==maxy or i[0]==maxx) :
            validVoisin.append(mat[i[0]][i[1]])
    return(validVoisin.count("#"))



print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp:
        mat=[]
        for i in inp :
            mat.append(list(i[:-1]))
        maxy=len(mat[0])
        maxx=len(mat)
        newmat=copy.deepcopy(mat)
        c=0
        for i in mat :
            print("".join(i))
        while True:
            change=False
            x=0
            while x<maxx :
                y=0
                while y<maxy :
                    if mat[x][y]=="." :
                        y+=1
                        continue
                    elif mat[x][y]=="L" :
                        if nVoisinVisi(mat,x,y)==0 :
                            newmat[x][y]="#"
                            change=True
                    elif mat[x][y]=="#" :
                        if nVoisinVisi(mat,x,y)>=5 :
                            newmat[x][y]="L"
                            change=True
                    y+=1
                x+=1
            mat=copy.deepcopy(newmat)
            print()
            for i in newmat :
                print("".join(i))
            c+=1
            if not change :
                k=0
                for i in mat :
                    k+=i.count("#")
                return(k)

def nVoisinVisi(mat,x,y) :
    maxy=len(mat[0])
    maxx=len(mat)
    voisin=[]
    v="."
#    while v=="." :
    voisin.append((0,(x-1,y-1)))
    voisin.append((1,(x-1,y)))
    voisin.append((2,(x-1,y+1)))
    voisin.append((3,(x,y-1)))
    voisin.append((4,(x,y+1)))
    voisin.append((5,(x+1,y-1)))
    voisin.append((6,(x+1,y)))
    voisin.append((7,(x+1,y+1)))
    validVoisin=[]
    for i in voisin :
        if not(-1 in i[1] or i[1][1]==maxy or i[1][0]==maxx) :
            validVoisin.append((i[0],mat[i[1][0]][i[1][1]]))
    o=[x[1] for x in validVoisin].count(".")
    c=0
    while o : 
#        if x==0 and y==6 :
#            print("--------------c--------------")
#            print(c)
#            print("\nvalid lol")
#            print(validVoisin)
#            print("\nvoisinlol")
#            print(voisin)
#            print("\n")
        newValid=[]
        for i in validVoisin :
            if i[1]=="." :
                coord=voisin[i[0]][1]
#                if x==0 and y==6 :
#                    print("\nvoisin i00")
#                    print(voisin[i[0]])
#                    print(x)
#                    print(coord)

                if i[0]==0:
                    nx=coord[0]-1
                    ny=coord[1]-1
                if i[0]==3:
                    nx=coord[0]
                    ny=coord[1]-1
                if i[0]==5:
                    nx=coord[0]+1
                    ny=coord[1]-1
                if i[0]==1:
                    nx=coord[0]-1
                    ny=coord[1]
                if i[0]==6:
                    nx=coord[0]+1
                    ny=coord[1]
                if i[0]==2:
                    nx=coord[0]-1
                    ny=coord[1]+1
                if i[0]==4:
                    nx=coord[0]
                    ny=coord[1]+1
                if i[0]==7:
                    nx=coord[0]+1
                    ny=coord[1]+1
#                if x==0 and y==6 :
#                    print(i)
#                    print(nx)
#                    print(ny)
#                    print(voisin)
                if not(nx<=-1 or ny<=-1 or ny>=maxy or nx>=maxx) :
                    voisin[i[0]]=(i[0],(nx,ny))
                    newValid.append((i[0],mat[nx][ny]))
#                    if x==0 and y==6 :
#                        print("loooooooooooooooool")
#                        print((i[0],mat[nx][ny]))
#                        print(voisin)
            else:
                newValid.append(i)
        validVoisin=copy.deepcopy(newValid)
        c+=1
        o=[x[1] for x in validVoisin].count(".")
#        if x==0 and y==6 :
#            print("valid")
#            print(validVoisin)
#            print(o)
    y=[x[1] for x in validVoisin].count("#")
#    if x==0 and y==6 :
#        print(o)
    return(y)


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
