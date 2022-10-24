import sys

def partOne(inpu) :
    with open(inpu,'r') as inp :
        tree=0
        mat=[]
        for i in inp :
            mat.append(list(i[:-1]))
        x=0
        y=0
        while y<len(mat)-1 :
            x+=3
            if x>=len(mat[y]) :
                x-=len(mat[y])
            y+=1
            if mat[y][x]=="#" :
                tree+=1
    return tree




print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()


def partTwo(inpu) :
    with open(inpu,'r') as inp :
        trees=[]
        mat=[]
        for i in inp :
            mat.append(list(i[:-1]))
        slope=[(1,1),(3,1),(5,1),(7,1),(1,2)]
        for j in slope : 
            x=0
            y=0
            tree=0
            while y<len(mat)-1 :
                x+=j[0]
                if x>=len(mat[y]) :
                    x-=len(mat[y])
                y+=j[1]
                if mat[y][x]=="#" :
                    tree+=1
            trees.append(tree)
    treesMultiply=1
    for i in trees :
        treesMultiply*=i
    return treesMultiply

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


