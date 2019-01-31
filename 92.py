#rubi
n=int(input())
l=[int(i) for i in input().split()]
sum=0
for num in range(0,len(l)):
	sum=sum+l[num]
print(sum)	
