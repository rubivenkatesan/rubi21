n=input()
l=list(map(int,input().split()))
c=0
k=0
for i in range(0,len(l)):
        if l[i]%2==0:
                c=c+1
                d=l[i]
        else:
                k=k+1
                di=l[i]
if c==1:
        print(d)
else:
        print(di)
# rubi
