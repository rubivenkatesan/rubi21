#rubi
n=int(input())
l=[str(i) for i in input().split()]
for i in range(n):
	if l.count(l[i])==1:
		print(l[i])
		break
