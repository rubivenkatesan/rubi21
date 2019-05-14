#rubi
n,k=map(int,input().split())
l=list(map(int,input().split()))
s=""
for i in range(0,k):
        l.remove(l[-1])
for i in range(0,len(l)):
        s=s+str(l[i])+" "
print(s.strip())
