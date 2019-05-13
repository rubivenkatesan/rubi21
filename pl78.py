n,k=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
p=l+m
p.sort()
s=""
for i in range(0,len(p)):
        s=s+str(p[i])+" "
print(s.strip())
#merge
