#rubi
s=input()
s=s[::-1]
t=""
for i in range(len(s)-1):
	t+=s[i]+"-"
print(t+s[len(s)-1])
