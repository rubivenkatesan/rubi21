#rubi
n=int(input())
m=list(map(int,input().split()))
s=[]
for i in range(n-1):
  s.append(m[i]+m[i+1])
print(max(s))  
