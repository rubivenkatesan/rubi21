#rubi
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
s=""
for i in range(0,len(a)):
  if(a[i]<k):
    
    s=s+str(a[i])+" "
    
    
   
print(s.strip())    
