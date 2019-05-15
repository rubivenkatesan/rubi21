#int
a=input()
sum=0
for i in a:
 sum=sum+int(i)
k=str(sum)
if(k==k[::-1]):
 print("YES")
else:
 print("NO")
