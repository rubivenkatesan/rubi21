#rubi
s=input()
k=""
l=[]
for i in s:
	l.append(s.count(i))
min1=min(l)
for i in s:
	if s.count(i)==min1 and i!=" ":
		k=k+i.lower()+" "
print(k.strip())
