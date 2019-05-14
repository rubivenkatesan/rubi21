#rubi
h=int(input())
m=0
a=list(map(int,input().split()))
for y in range(0,h):
  for x in range(0,y):
    if(a[x]<a[y]):
      m=m+a[x]
print(m)
