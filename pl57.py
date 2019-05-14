#rubi
n,k=map(str,input().split())
c=0
for i in range(len(n)):
  if k==n[i]:
    c+=1
print(c)    
