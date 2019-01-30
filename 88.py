#rubi
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)
n,m=map(int,input().split())
p=gcd(n,m)
lcm=n*m//p
print(lcm)
