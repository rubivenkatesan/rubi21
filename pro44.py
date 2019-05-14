#rubi
n,p,q,r=map(int,input().split())
l=list(map(int,input().split()))
t=[]
for i in range(0,n):
	for j in range(i,n):
		for k in range(j,n):
			a=p*l[i]+q*l[j]+r*l[k]
			l.append(a)
print(max(l))
