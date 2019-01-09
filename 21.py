#rubi
n=int(input())
a=int(input())
d=int(input())
sum=0
for i in range(0,n):
  sum+=a
  a+=d
  i+=1
print(sum)  
