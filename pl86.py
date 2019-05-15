#rubi
n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(n-1):
  s.append(l[i]^l[i+1])
print(*s)  
