#rub
n=int(input())
l=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
b=[]
for i in range(n):
	b.append(l[i]+a[i])
print(*b)
