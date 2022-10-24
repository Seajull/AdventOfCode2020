import sys

def partOne(inpu) :
    with open(inpu,'r') as inp :
        listL=[]
        listP=[]
        an=2020
        for i in inp :
            n=int(i[:-1])
            if n > an/2 :
                listL.append(n)
            else :
                listP.append(n)
        for i in listL :
            for j in listP :
                if i+j == 2020 :
                    return(i*j)


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

import itertools

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        li=[]
        for i in inp :
            n=int(i[:-1])
            li.append(n)
        c=list(itertools.combinations(li,3))
        for i in c :
            if sum(i)==2020 :
                return(i[0]*i[1]*i[2])

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


