import sys, re, copy 

# RPN stuff with Shunting_yard_algorithm
# https://en.wikipedia.org/wiki/Shunting_yard_algorithm

def partOne(inpu) :
    with open(inpu,'r') as inp:
        sumtotal=0
        for op in inp :
            op=op[:-1]
            op=op.replace(" ","")
            out=[]
            stack=[]
            for i in op :
                try:
                    i=int(i)
                    out.append(i)
                except :
                    if stack : 
                        if i==")" :
                            while stack[-1]!="(" :
                                out.append(stack[-1])
                                del(stack[-1])
                            del(stack[-1])
                        else :
                            if i!="(" and stack[-1]!="(" :
                                out.append(stack[-1])
                                del(stack[-1])
                            stack.append(i)
                    else :
                        stack.append(i)
            c=len(stack)-1
            while c>=0 :
                out.append(stack[c])
                c-=1
            sumtotal+=decodeRPN(out)
        return sumtotal

def decodeRPN(rpn) :
    stack=[]
    for i in rpn :
        if isinstance(i,int):
            stack.append(i)
        else :
            a=stack.pop(-1)
            b=stack.pop(-1)
            stack.append(eval(str(b)+i+str(a)))
    return stack[0]

print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp:
        sumtotal=0
        for op in inp :
            op=op[:-1]
            op=op.replace(" ","")
            out=[]
            stack=[]
            for i in op :
                try:
                    i=int(i)
                    out.append(i)
                except :
                    if stack : 
                        if i=="*" and stack[-1]=="+":
                            out.append(stack[-1])
                            del(stack[-1])
                            stack.append(i)
                        elif i==")" :
                            while stack[-1]!="(" :
                                out.append(stack[-1])
                                del(stack[-1])
                            del(stack[-1])
                        else :
                            if (i!="(" and stack[-1]!="(") and i==stack[-1] :
                                out.append(stack[-1])
                                del(stack[-1])
                            stack.append(i)
                    else :
                        stack.append(i)
            c=len(stack)-1
            while c>=0 :
                out.append(stack[c])
                c-=1
            sumtotal+=decodeRPN(out)
        return sumtotal

def decodeRPN(rpn) :
    stack=[]
    for i in rpn :
        if isinstance(i,int):
            stack.append(i)
        else :
            a=stack.pop(-1)
            b=stack.pop(-1)
            stack.append(eval(str(b)+i+str(a)))
    return stack[0]

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()
