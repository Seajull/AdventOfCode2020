import sys, re

def partOne(inpu) :
    with open(inpu,'r') as inp:
        dic={}
        for i in inp :
            con=re.search("(\w+ \w+) bag[s]? contain",i)
            if "contain no other" in i :
                dic[con.group(1)]=""
            else :
                res=re.findall("\d (\w+ \w+) bag[s]?",i)
                dic[con.group(1)]=res
        return getBig(dic,["shiny gold"])

def getBig(dic,bag,counter=[]) :
    bagtc=[]
    for b in bag :
        for i in dic :
            if b in dic[i] :
                bagtc.append(i)
    counter+=bagtc
    if bagtc :
        return getBig(dic,bagtc,counter)
    else :
        return len(set(counter))


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp:
        dic={}
        for i in inp :
            con=re.search("(\w+ \w+) bag[s]? contain",i)
            if "contain no other" in i :
                dic[con.group(1)]=""
            else :
                res=re.findall("(\d+) (\w+ \w+) bag[s]?",i)
                dic[con.group(1)]=res
        return getBig2(dic,[("0","shiny gold")])


# Nice readable code right here ;) 

def getBig2(dic,bag,bigbag=[]):
    bagtc=[]
    bigbag+=bag
    for b in bag :
        multi=int(b[0])
        if multi==0 :
            multi+=1
        for i in dic[b[1]] :
            i=(int(i[0])*multi,i[1])
            bagtc.append(i)
    if bagtc :
        return getBig2(dic,bagtc)
    else : 
        counter=0
        for i in bigbag :
            counter+=int(i[0]) 
        return counter


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
