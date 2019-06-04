#rubi
n,k=map(str,input().split())
k=int(k)
l=[]
for i in range(len(n)-k+1):
	l.append(n[i:i+k])
print(*l)
