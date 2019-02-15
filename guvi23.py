#rubi
n,k=map(int,input().split())
l=list(map(int,input().split()))
s=list(map(int,input().split()))
k=""
for i in s:
    l.append(i)
    k=k+str(max(l))+" "
print(k.strip())
