import sys

def partOne(inpu) :
    with open(inpu,'r') as inp :
        passeport=[]
        valid=0
        for i in inp :
            if not i[:-1] : 
                passeport=[x[0:3] for sub in passeport for x in sub]
                if len(passeport)==8 or (len(passeport)==7 and "cid" not in passeport) :
                    valid+=1
                passeport=[]
            else :
                passeport.append(i[:-1].split(" "))
        passeport=[x[0:3] for sub in passeport for x in sub]
        if len(passeport)==8 or (len(passeport)==7 and "cid" not in passeport) :
            valid+=1
    return valid



print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

import re
def partTwo(inpu) :
    with open(inpu,'r') as inp :
        passeport=[]
        pv=0
        listPasseport=[]
        valid=0
        for i in inp :
            if not i[:-1] : 
                passeport=[x for sub in passeport for x in sub]
                listPasseport.append(passeport)
                passeport=[]
            else :
                passeport.append(i[:-1].split(" "))
        passeport=[x for sub in passeport for x in sub]
        listPasseport.append(passeport)
        
        for pp in listPasseport :
            dicpp={}
            for item in pp :
                dicpp[item.split(":")[0]]=item.split(":")[1]
            valid=0

            if len(dicpp)==8 or (len(dicpp)==7 and "cid" not in dicpp.keys()) :
                pass
            else :
                continue

            if 1920 <= int(dicpp["byr"]) <= 2002 :
                valid+=1
            else :
                continue

            if 2010 <= int(dicpp["iyr"]) <= 2020 :
                valid+=1
            else :
                continue

            if 2020 <= int(dicpp["eyr"]) <= 2030 :
                valid+=1
            else :
                continue

            if "cm" in dicpp["hgt"] :
                if 150 <= int(dicpp["hgt"][:-2]) <= 193 :
                    valid+=1
            elif "in" in dicpp["hgt"] :
                if 59 <= int(dicpp["hgt"][:-2]) <= 76 :
                    valid+=1
            else :
                continue

            if dicpp["hcl"][0]=="#" and len(dicpp["hcl"])==7 :
                res=re.search("\w{9}",dicpp["hcl"])
                if res :
                    valid+=1
            else :
                continue

            if dicpp["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"] :
                valid+=1
            else :
                continue

            if len(dicpp["pid"])==9 :
                res=re.search("\d{9}",dicpp["pid"])
                if res :
                    valid+=1
            else :
                continue

            if valid == 6 :
                pv+=1
    return pv

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


