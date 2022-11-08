import sys, re, copy 

def partOne(inpu) :
    with open(inpu,'r') as inp:
        som=0
        dic={}
        for i in inp :
            if "mask" in i :
                mask=i[:-1].split(" = ")[1]
            else :
                res=re.search("mem\[(\d+)\] = (\d+)",i)
                if res :
                    mem=int(res.group(1))
                    val=int(res.group(2))
                valbin=format(val,"036b")
                c=0
                valmasked=""
                while c<len(mask) :
                    if mask[c]=="X" :
                        valmasked+=valbin[c]
                    else :
                        valmasked+=mask[c]
                    c+=1
                dic[mem]=int(valmasked,2)
        som+=sum(dic.values())
        return som


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp:
        som=0
        dic={}
        for i in inp :
            if "mask" in i :
                mask=i[:-1].split(" = ")[1]
            else :
                res=re.search("mem\[(\d+)\] = (\d+)",i)
                if res :
                    mem=int(res.group(1))
                    val=int(res.group(2))
                membin=format(mem,"036b")
                c=0
                binmasked=""
                while c<len(mask) :
                    if mask[c]=="X" :
                        binmasked+="X"
                    elif mask[c]=="0" :
                        binmasked+=membin[c]
                    elif mask[c]=="1" :
                        binmasked+=mask[c]
                    c+=1
                address=[]
                address.append(binmasked)
                while True :
                    find=False 
                    newaddress=[]
                    for i in address :
                        c=0
                        while c<len(i) :
                            if i[c]=="X" :
                                find=True
                                newaddress.append(i[:c]+"0"+i[c+1:])
                                newaddress.append(i[:c]+"1"+i[c+1:])
                                break
                            c+=1
                    if not find :
                        break
                    else :
                        address=list(newaddress)
                for i in address :
                    dic[int(i,2)]=val
        return sum(dic.values())




print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()
