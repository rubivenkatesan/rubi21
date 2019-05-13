n=int(input())
l=[int(i) for i in input().split()]
c=0
for i in range(len(l)):
  for j in range(len(l)):
    if l[i]<l[j]:
      c+=1
    
print(c)    
# rubi
