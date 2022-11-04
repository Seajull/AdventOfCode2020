import sys, re, itertools

def partOne(inpu) :
    with open(inpu,'r') as inp:
        j=[]
        for i in inp :
            j.append(int(i[:-1]))
        j=sorted(j)
        last=0
        j1=0
        j3=0
        for i in j :
            if i-last==1:
                j1+=1
            elif i-last==3 :
                j3+=1
            last=i
        j3+=1
        return j1*j3


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp:
        j=[]
        for i in inp :
            j.append(int(i[:-1]))
        j.append(0)
        j=sorted(j)
        j.append(j[-1]+3)
        dic={}
        for i in j :
            c=1
            while c<4 :
                if i-c in j : 
                    if i in dic.keys() :
                        dic[i].append(i-c)
                    else :
                        dic[i]=[i-c]
                c+=1
        newdic={}
#        k=0
        newdic[0]=1
        for i in dic :
            if dic[i]==[0] :
                newdic[i]=1
                continue
            newdic[i]=0
            for k in dic[i] :
                newdic[i]+=newdic[k]
        return(newdic[j[-1]])


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
