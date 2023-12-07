import sys, re, copy 

def partOne(inpu) :
    with open(inpu,'r') as inp:
        rule={}
        message=[]
        ism=False
        for line in inp :
            if line=="\n" :
                ism=True
            elif ism :
                message.append(line[:-1])
            else :
                lines=line[:-1].split(": ")
                if "a" in lines[1] :
                    rule[lines[0]]="a"
                    a=lines[0]
                elif "b" in lines[1] :
                    rule[lines[0]]="b"
                    b=lines[0]
                else :
                    subrule=lines[1].split(" | ")
                    sub=[]
                    for i in subrule :
                        sub.append(i.split(" "))
                    rule[lines[0]]=sub
        print(rule)
        print(a,b)
        print(message)
        start="0"
        cur=rule[start]
        print(cur)
        cont=True
        while cont :
            newcur=[[]]
            input("\nContinue ?\n")
            for i in cur:
                for e in i :
                    if e in [a,b] :
                        for l in newcur :
                            l.append(e)
                    else :
                        if len(rule[e])==2 :  
                            print(rule[e])
                            newcur=newcur+copy.deepcopy(newcur)
                            c=0
                            while c<len(newcur):
                                if c<len(newcur)/2 :
                                    newcur[c].append(rule[e][0])
                                else :
                                    newcur[c].append(rule[e][1])
                                c+=1
                        else :
                            c=0
                            while c<len(newcur):
                                if c<len(newcur)/2 :
                                    newcur[c].append(rule[e][0])
                                else :
                                    newcur[c].append(rule[e][1])
                                c+=1
            res=re.findall("\d",str(newcur))
            cont=False
            print(newcur)
            for let in res : 
                if let not in [a,b] :
                    cont=True
            print()
            print(newcur)
            m=[]
            for it in newcur :
                m.append(re.findall("\d+",str(it)))
            newcur=copy.deepcopy(m)
            cur=copy.deepcopy(newcur)
            print()
            print(cur)
        possible=[]
        for i in newcur :
            l=""
            for j in i :
                if j==a :
                    l+="a"
                elif j==b :
                    l+="b"
            possible.append(l)
        print(possible)

    return




print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp:
        return

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()
