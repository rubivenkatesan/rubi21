#RUBI
r,s=map(int,input().split())
l=[int(i) for i in input().split()]
t=[int(i) for i in input().split()]
f=1
for i in range(s):
	if t[i] in l:
		f=1
	else:
		f=0
print("YES" if f==1 else "NO")
