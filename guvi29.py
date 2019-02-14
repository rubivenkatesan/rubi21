#rubi
l,r=map(int,input().split())
c=0
for i in range(l,r+1):
    for j in range(1,100):
        if j*j==i:
            c=c+1
print(c)
