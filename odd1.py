#rubi
n,k=map(int,input().split(" "))
l=[i for i in range(n+1,k) if (i%2)!==0]
k=[print(l[i],end=" ")for i in range(0,len(l)-1)]
print(l[len(l)-1])
