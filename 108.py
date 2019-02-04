#rubi
n,k=map(int,input().split())
l=list(map(int,input().split()))
s=sorted(l)
c=0
for i in range(0,len(s)):
	c=c+1
	if c==k:
		print(s[i])
