#rubi
n=int(input())
a=list(map(int,input().split()))
t=max(a)
c,d=0,0
for i in range(0,len(a)-1):
  for j in range(i+1,len(a)):
    if abs(a[i]+a[j])<t:
      c,d=a[i],a[j]
      t=abs(c+d)
print(c,d)
