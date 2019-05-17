#rubi
n=int(input())
a=list(map(int,input().split()))

l=[]

for i in range(0,n-1):
  l.append(a.count(i))
print(max(l))  
