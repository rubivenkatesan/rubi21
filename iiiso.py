#rubi
s1,s2=map(str,input().split())
c=[]
d=[]
for i in s1:
	c.append(s1.count(i))
for j in s2:
	d.append(s2.count(j))
for i in c:
	if i in d:
		flag=1
	
	else:
		flag=0
if flag==1:
	print("yes")
else:
	print("no")
