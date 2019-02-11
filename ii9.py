#rubi
l,m=map(int,input().split())
c=0
for i in range(l,m+1):
	for j in range(2,i):
		if i%j==0:
			break
	else:
	    c=c+1
print(c)
