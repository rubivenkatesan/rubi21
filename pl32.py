#rubi
n,q=map(int,input().split())
l=list(map(int,input().split()))
res=0
for i in range(len(l)):
  if (l[i]==q):
    res+=1
    print("Yes")
    break
else:
  print("No")

     
