#rubi
n=int(input())
l=[]
flag=1
a=[]
s=""
for i in range(2,n+1):
    for j in range(2,n+1):
        if i*j==n:
            l.append(i)
for i in l:
    for j in range(2,i):
        if i%j==0:
            flag=0
            break
        else:
            flag=1
    if flag==1:
        s=s+str(i)+" "
print(s.strip())
