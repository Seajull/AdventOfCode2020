import sys, re, copy 

def partOne(inpu) :
    with open(inpu,'r') as inp:
        c=0
        listRang=[]
        ticket=[]
        for i in inp : 
            if i=="\n" :
                c+=1
                continue
            if c==0 :
                rang=i[:-1].split(": ")[1].split(" or ")
                rang=[(x.split("-")) for x in rang]
                rang=[(int(i[0]),int(i[1])) for i in rang]
                listRang.append(rang)
            if c==2: 
                if i[0]!="n":
                    tic=i[:-1].split(",")
                    tic=[int(j) for j in tic]
                    ticket.append(tic)
    valid=[]
    for i in ticket :
        for n in i :
            for rang in listRang:
                if not(n not in range(rang[0][0],rang[0][1]+1) and n not in range(rang[1][0],rang[1][1]+1)) :
                    if n not in valid :
                        valid.append(n)
    unvalid=[]
    for i in ticket :
        for n in i :
            if n not in valid :
                unvalid.append(n)
    return sum(unvalid)


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
'''
It work but way to much cluttered
'''
    with open(inpu,'r') as inp:
        c=0
        field=[]
        listRang=[]
        ticket=[]
        for i in inp : 
            if i=="\n" :
                c+=1
                continue
            if c==0 :
                rang=i[:-1].split(": ")[1].split(" or ")
                field.append(i.split(": ")[0])
                rang=[(x.split("-")) for x in rang]
                rang=[(int(i[0]),int(i[1])) for i in rang]
                listRang.append(rang)
                
            elif c==1 :
                if i[0]!="y":
                    myticket=i[:-1].split(",")
                    myticket=[int(j) for j in myticket]
            elif c==2: 
                if i[0]!="n":
                    tic=i[:-1].split(",")
                    tic=[int(j) for j in tic]
                    ticket.append(tic)
    valid=[]
    for i in ticket :
        for n in i :
            for rang in listRang:
                if not(n not in range(rang[0][0],rang[0][1]+1) and n not in range(rang[1][0],rang[1][1]+1)) :
                    if n not in valid :
                        valid.append(n)
    unvalid=[]
    ticketValid=copy.deepcopy(ticket)
    for i in ticket :
        for n in i :
            if n not in valid :
                unvalid.append(n)
                ticketValid.remove(i)
    
    ticketValid=([list(x) for x in zip(*ticketValid)])
    posi=[]
    for i in ticketValid :
        c=0
        posi.append([])
        for n in i :
            posi[-1].append([])
            for rang in listRang:
                if not(n not in range(rang[0][0],rang[0][1]+1) and n not in range(rang[1][0],rang[1][1]+1)):
                    posi[-1][-1].append(1)
                else :
                    posi[-1][-1].append(0)
    dic=[]
    num=0
    for i in posi :
        i=[list(x) for x in zip(*i)]
        dic.append([num])
        dic[-1].append([])
        for j in i :
            if 0 in j :
                dic[-1][1].append(0)
            else :
                dic[-1][1].append(1)
        num+=1
    dic.sort(key=lambda x:sum(x[1]))
    dicPos={}
    for i in dic :
        num=i[0]
        c=0
        for n in i[1] :
            if n==1:
                if field[c] not in dicPos.keys() :
                    dicPos[field[c]]=num
                    break
            c+=1
    mult=1
    for i in dicPos.keys() :
        if i[0:9] =="departure" :
            mult=mult*myticket[dicPos[i]]
    return mult

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()
