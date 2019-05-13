#rubi
a=list(input())
b={'\0'}
c=[]
tmp=1
for i in range(0,len(a)):
    b.add(a[i])
    if(tmp!=len(b)):
        c.append(a[i])
        tmp=len(b)
for i in range(0,len(c)):
    if(i!=len(c)-1):
        print(c[i],end="")
    else:
        print(c[i])
