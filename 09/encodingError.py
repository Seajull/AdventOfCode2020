import sys, re, itertools

def partOne(inpu) :
    with open(inpu,'r') as inp:
        num=[]
        for i in inp :
            num.append(int(i[:-1]))
        c=0
        while c<len(num) :
            if c>=25 :
                combi=[sum(x) for x in (list(itertools.combinations(num[c-25:c],2)))]
                if num[c] not in combi :
                    return(num[c])
            c+=1


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp:
        num=[]
        for i in inp :
            num.append(int(i[:-1]))
        c=0
        inv=0
        while c<len(num) :
            if c>=25 :
                combi=[sum(x) for x in (list(itertools.combinations(num[c-25:c],2)))]
                if num[c] not in combi :
                    inv=num[c]
                    break
            c+=1
        c=0
        temp=[]
        while c<len(num) :
            p=c
            while sum(temp)<inv :
                temp.append(num[p])
                p+=1
            if sum(temp)==inv :
                break
            else :
                temp=[]
                c+=1
        return(min(temp)+max(temp))


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
