import sys, re, copy 

def partOne(inpu) :
    turn=0
    with open(inpu,'r') as inp:
        dic={}
        start=inp.readline()[:-1].split(",")
        while turn<2020 :
            if turn<len(start) :
                spoken=int(start[turn%len(start)])
                dic[spoken]=(turn+1,0)
            else :
                if dic[spoken][1]==0 :
                    spoken=0
                    dic[spoken]=(turn+1,dic[spoken][0])
                else :
                    spoken=dic[spoken][0]-dic[spoken][1]
                    if spoken not in dic.keys() :
                        dic[spoken]=(turn+1,0)
                    else :
                        dic[spoken]=(turn+1,dic[spoken][0])
            turn+=1
        return spoken


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    turn=0
    with open(inpu,'r') as inp:
        dic={}
        start=inp.readline()[:-1].split(",")
        while turn<30000000 :
            if turn<len(start) :
                spoken=int(start[turn%len(start)])
                dic[spoken]=(turn+1,0)
            else :
                if dic[spoken][1]==0 :
                    spoken=0
                    dic[spoken]=(turn+1,dic[spoken][0])
                else :
                    spoken=dic[spoken][0]-dic[spoken][1]
                    if spoken not in dic.keys() :
                        dic[spoken]=(turn+1,0)
                    else :
                        dic[spoken]=(turn+1,dic[spoken][0])
            turn+=1
        return spoken

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()
