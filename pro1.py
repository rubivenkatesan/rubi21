#rubi
a=int(input())
s=[]
for i in range(a):
	s.append([])
for i in range(a):
	q=input()
	s[i].append(q)
mini=len(s[0][0])
for i in range(a):
	if len(s[i][0])<mini:
		mini=len(s[i][0])
res=""
for i in range(mini):
	flag=True
	for j in range(a-1):
		if s[j][0][i]!=s[j-1][0][i]:
			flag=False
			break
	if flag:
		res+=s[a-1][0][i]
	else:
		break
print(res)
