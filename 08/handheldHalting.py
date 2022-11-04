import sys, re

def partOne(inpu) :
    with open(inpu,'r') as inp:
        code=[]
        for i in inp :
            isp=i[:-1].split(" ")
            code.append((isp[0],int(isp[1])))
        p=0
        acc=0
        visited=[]
        while p<len(code) :
            if p in visited :
                break
            else :
                visited.append(p)
            if code[p][0]=="nop" :
                p+=1
            elif code[p][0]=="acc":
                acc+=code[p][1]
                p+=1
            elif code[p][0]=="jmp" :
                p+=code[p][1]
        return acc


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp:
        code=[]
        for i in inp :
            isp=i[:-1].split(" ")
            code.append((isp[0],int(isp[1])))
    c=0
    totest=[]
    for i in code :
        if i[0]=="nop" or i[0]=="jmp" :
            totest.append(c)
        c+=1
    c=0
    ogcode=code.copy()
    while isLooped(code)[1] :
        code=ogcode.copy()
        if code[totest[c]][0]=="nop" :
            code[totest[c]]=("jmp",code[totest[c]][1])
        else :
            code[totest[c]]=("nop",code[totest[c]][1])
        c+=1
    
    return isLooped(code)[0]



def isLooped(code) :
    p=0
    acc=0
    visited=[]
    oldP=0
    looped=False
    while p<len(code) :
        if p in visited :
            looped=True
            break
        else :
            visited.append(p)
        if code[p][0]=="nop" :
            p+=1
        elif code[p][0]=="acc":
            acc+=code[p][1]
            p+=1
        elif code[p][0]=="jmp" :
            p+=code[p][1]
    return acc,looped


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
