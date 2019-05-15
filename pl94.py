#rubi
n=int(input())
c=0
for i in range(n-1):
  c+=1
  if(c>1):
    print("yes")
    break
else:
  print("no")    
