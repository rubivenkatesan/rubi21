#rubi
n,k=map(int,input().split())
l=[int(i) for i in input().split()]
c=0
for i in range(n):
	for j in range(i+1,n):
		if abs(l[i]-l[j])==k:
			c+=1
print(c)
