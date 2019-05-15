#rubi
m=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in range(0,m):
  c+=a[i-1]
  b.append(c)
print(*b[::-1])  
  
