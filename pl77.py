n=int(input())
l=list(map(int,input().split()))
c=1
p=[]
for i in range(0,len(l)-1):
        if l[i]<l[i+1]:
                c=c+1
        else:
               p.append(c)
               c=1
p.append(c)
print(max(p))
# rubi
