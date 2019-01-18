#rubi
n,k=map(int,input().split(" "))
l=[int(i) for i in input().split()]
c=0
for i in l:
  if i==k:
    c=c+1
print(c)
