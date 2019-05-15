#rubi
m,n=map(str,input().split())
for i in m:
	if i in n:
		print('yes')
		break
else:
	print('no')
