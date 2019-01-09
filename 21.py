#rubi
n,a,d= map(int, input().split())

sum=0
for i in range(0,n):
  sum+=a
  a+=d
  i+=1
print(sum)  
