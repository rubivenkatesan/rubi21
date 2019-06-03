#ru
n,k=map(int,input().split())
l=[int(i) for i in input().split()]
c=1
for i in range(n):
	for j in range(i+1,n):
		if l[i]+l[j]==k:
			print("YES")
			c=1
			break
		else:
			c=0
	if c==1:
		break
if c==0:
	print("NO")
