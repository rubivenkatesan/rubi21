#rubi
r=int(input())
a=[]
k=bin(2**r-1)[2::]
l=len(k)
for i in range(0,2**r):
	s=bin(i)[2::]
	if len(s)<l:
		a.append([s.count("1"),(l-len(s))*"0"+s])
	else:
		a.append([s.count("1"),s])
a.sort()
for i in range(0,len(a)):
	print(a[i][1])
