#rubi
n=int(input())
k=list(map(int,input().split()))
s=""
for i in range(0,len(k)):
  if(k[i]<n):
    
    s=s+str(k[i])+" "
print(s.strip())        
    
   
  
