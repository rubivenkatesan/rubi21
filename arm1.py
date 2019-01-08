#rubi
n,k=map(int,input().split(" "))
l=[]
for i in range(n,k):
 t=i
 c=0
 arm=0
 rem=0
 c=len(str(n))
 while(t!=0):
  rem=t%10
  t=t//10
  arm=arm+(rem**c)
 if arm==i:
  l.append(i)
k=[print(l[i],end=" ")for i in range(0,len(l)-1)]
print(l[len(l)-1])
