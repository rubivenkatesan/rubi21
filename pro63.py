#rubi
s=input()
l=[]
for i in s:
	if i not in l:
		l.append(i)
	else:
		break
print(len(l))
