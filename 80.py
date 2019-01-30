#rubi
n=int(input())
l=list(str(n))
s=""
for i in range(0,len(l)):
	if int(l[i])%2!=0:
		s=s+l[i]+" "
print(s.rstrip())
