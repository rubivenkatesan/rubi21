#rubi
a,b,k=map(str,input().split())
k=int(k)
a=sorted(a)
b=sorted(b)
c=max(len(a),len(b))
count=0
for i in range(c):
    if a[i]!=b[i]:
        count=count+1
if count==k:
    print("yes")
else:
    print("no")
