import sys

def partOne(inpu) :
    with open(inpu,'r') as inp :
        valid=0
        for i in inp :
            isp=i[:-1].split(": ")
            n=isp[0][:-2].split("-")
            mini=int(n[0])
            maxi=int(n[1])
            letter=isp[0][-1]
            if mini <= isp[1].count(letter) <= maxi :
                valid+=1
        return valid



print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()


def partTwo(inpu) :
    with open(inpu,'r') as inp :
        valid=0
        for i in inp :
            c=0
            isp=i[:-1].split(": ")
            n=isp[0][:-2].split("-")
            x=int(n[0])-1
            y=int(n[1])-1
            letter=isp[0][-1]
            if isp[1][x]==letter :
                c+=1
            if isp[1][y]==letter :
                c+=1
            if c==1 :
                valid+=1
        return valid

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


