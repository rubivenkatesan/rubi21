#sorting
s=int(input())
t=[]
u=[]
for i in range(0,s):
  t=sorted(list(map(int,input().split())))
  u+=t
print(*sorted(u))  
