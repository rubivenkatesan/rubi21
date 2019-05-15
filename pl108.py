#rubi
m=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in range(0,m):
  c+=a[i]
  b.append(c)
print(*b)  
  
