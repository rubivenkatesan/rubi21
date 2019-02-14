#rubi
n,k=map(int,input().split())
s=max(n,k)
for i in range(1,s):
	if n%i==0 and k%i==0:
		a=i
if n==1 and k==1:
    a=1
print(a)
