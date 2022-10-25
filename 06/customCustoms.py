import sys

def partOne(inpu) :
    with open(inpu,'r') as inp:
        allg=[]
        g=[]
        for i in inp :
            if i[:-1] :
                g.append(i[:-1])
            if not i[:-1] :
                allg.append(g)
                g=[]
        allg.append(g)
        g=[]
        c=0
        for i in allg :
            c+=(len(set("".join(i))))
    return c



print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp:
        allg=[]
        g=[]
        for i in inp :
            if i[:-1] :
                g.append(i[:-1])
            if not i[:-1] :
                allg.append(g)
                g=[]
        allg.append(g)
        g=[]
        c=0
        for i in allg :
            gjoin="".join(i)
            dic={}
            for l in gjoin :
                if l in dic.keys() :
                    dic[l]+=1
                else :
                    dic[l]=1
            for v in dic :
                if len(i) == dic[v] :
                    c+=1

    return c


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


